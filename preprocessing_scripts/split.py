#! /usr/bin/python3
import argparse
from collections import defaultdict
import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

stats_keys = ["male", "female",
              "neutral", "happiness", "sadness", "surprise", "questioning", "anger",
              "egy", "msa", "lav", "glf", "nor"]
data_percentages = {"all": {"test": 0.12, "dev": 0.12, "train": 1.1},
                    "mdas": {"test": 0.15, "dev": 0.15, "train": 1.1},
                    "king": {"test": 0.10, "dev": 0.10, "train": 1.1},
                    "qcri": {"test": 0.10, "dev": 0.10, "train": 1.1},
                    "ksu": {"test": 0.14, "dev": 0.14, "train": 1.1}}


def read_dataset(filename):
    db = {}
    stats = {k: 0 for k in stats_keys}
    with open(filename) as f:
        for line in f:
            utt_id, _, spk_id, gender, emotion, dialect = line.strip().split()
            if spk_id not in db:
                db[spk_id] = {"rows": [], "stats": {k: 0 for k in stats_keys}}
            db[spk_id]["rows"].append(line)
            for label in [gender, emotion, dialect]:
                if label != "0":
                    db[spk_id]["stats"][label] += 1
                    stats[label] += 1

    return db, stats


def split_dataset(db, stats, dataset, set_types=["test", "dev", "train"]):
    sets = defaultdict(list)
    if dataset in data_percentages:
        percentages = data_percentages[dataset]
    else:
        percentages = data_percentages["all"]

    used_spks = set()
    for set_type in set_types:
        set_stats = {k: 0 for k in stats_keys}
        for spk_id in db:
            if spk_id in used_spks:
                continue
            ratios = {k: (set_stats[k] + db[spk_id]["stats"][k]) / stats[k]
                      for k in stats_keys if stats[k] > 0}
            if all(v < percentages[set_type] for v in ratios.values()):
                used_spks.add(spk_id)
                set_stats = {k: set_stats[k] + db[spk_id]["stats"][k] for k in stats_keys}
                sets[set_type] += db[spk_id]["rows"]

    return sets


def combine_datasets(datasets):
    combined = defaultdict(list)
    for dataset in datasets:
        split_into = ["test", "dev", "train"]
        for set_type in ["test", "dev", "train"]:
            file_path = os.path.join(
                ROOT_PATH, "raw_data", dataset, "labels_{}.txt".format(set_type))

            if os.path.isfile(file_path):
                split_into.remove(set_type)
                combined[set_type] += open(file_path).readlines()

        db, stats = read_dataset("raw_data/{}/labels.txt".format(dataset))
        datasets = split_dataset(db, stats, dataset, set_types=split_into)
        for set_type in split_into:
            combined[set_type] += datasets[set_type]

    return combined


def print_stats(sets, dataset_names):
    stats = {d: {s: {l: 0 for l in stats_keys} for s in list(sets.keys()) + ["all"]}
             for d in dataset_names + ["all"]}
    for set_type in sets:
        for item in sets[set_type]:
            _, dataset, _, gender, emotion, dialect = item.strip().split("\t")
            for label in [gender, emotion, dialect]:
                if label != "0":
                    stats[dataset][set_type][label] += 1
                    stats[dataset]["all"][label] += 1
                    stats["all"]["all"][label] += 1
                    stats["all"][set_type][label] += 1

    print("\t".join(["Dataset", "Set Type", "Label", "Count", "Percentage"]))
    for dataset in dataset_names:
        for set_type in sets:
            for label in stats_keys:
                count = stats[dataset][set_type][label]
                if stats[dataset]["all"][label] == 0:
                    continue
                percentage = count / stats[dataset]["all"][label]
                print("\t".join([dataset, set_type, label, str(count), str(percentage)]))

    print("==============")
    print("\t".join(["Set Type", "Label", "Count", "Percentage"]))
    for set_type in sets:
        for label in stats_keys:
            count = stats["all"][set_type][label]
            percentage = count / stats["all"]["all"][label]
            print("\t".join([set_type, label, str(count), str(percentage)]))


def write_files(sets):
    for set_type in sets:
        file_path = os.path.join(ROOT_PATH, "data", "{}.txt".format(set_type))
        with open(file_path, "w") as f:
            for row in sets[set_type]:
                f.write(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--datasets', help='all raw files for splitting', nargs='*', type=str,
                        default=["ksu", "qcri", "sara", "anad", "mdas", "king"])
    args = parser.parse_args()
    sets = combine_datasets(args.datasets)
    print_stats(sets, args.datasets)
    write_files(sets)
