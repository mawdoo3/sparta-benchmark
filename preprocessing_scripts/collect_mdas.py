import os

path = '/data/asr-data/MDAS/'
utts = [i.strip() for i in open('utt2spk', 'r').readlines()]
dataset = "mdas"
utterances = []
d_dict = {'GULF': 'glf', 'MSA': 'msa', 'LEV': 'lav', 'EGY': 'egy'}

label_file = open("labels.txt", "w")
scp_file = open("wav.scp", "w")

for dialect_path in os.listdir(path):
    if os.path.isdir(os.path.join(path, dialect_path)):
        for wav in os.listdir(os.path.join(path, dialect_path)):
            if '.wav' in wav:
                temp = wav.split('_')
                utt_id = "-".join(temp)
                spk_id = "_".join([dataset, temp[0], temp[1]])
                gender = "0"
                emotion = "0"
                dialect = d_dict[temp[0]]
                abs_path = os.path.join(path, dialect_path, wav)

                label_file.write("\t".join(
                    [utt_id, dataset, spk_id, gender, emotion, dialect]) + "\n")
                scp_file.write("\t".join([utt_id, abs_path]) + "\n")

label_file.close()
scp_file.close()
