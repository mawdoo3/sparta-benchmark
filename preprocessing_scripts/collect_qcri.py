import os

path = '/data/asr-data/speech_profiling_data/dialect_detection/train.vardial2017/train_waves/'
test_path = '/data/asr-data/speech_profiling_data/dialect_detection/dev.vardial2017/dev_waves/'
test_map = "/data/asr-data/speech_profiling_data/dialect_detection/dev.vardial2017/wav.lst"

wav_label = {k.strip().split("/")[-1].replace("__", "-").replace("_", "-"): k.split("/")[-2].lower()
             for k in open(test_map)}

label_file = open("labels.txt", "w")
label_test_file = open("labels_test.txt", "w")
scp_file = open("wav.scp", "w")
dataset = "qcri"

for spk_id, wav in enumerate(os.listdir(path)):
    if '.wav' in wav:
        abs_path = os.path.join(path, wav)
        dialect = wav[:3].lower()
        spk_id = dataset + "-" + str(spk_id)
        gender = "0"
        emotion = "0"

        label_file.write("\t".join(
            [wav, dataset, spk_id, gender, emotion, dialect]) + "\n")
        scp_file.write("\t".join([wav, abs_path]) + "\n")


for spk_id, wav in enumerate(os.listdir(test_path)):
    if '.wav' in wav:
        abs_path = os.path.join(test_path, wav)
        dialect = wav_label[wav]
        spk_id = dataset + "-" + str(spk_id)
        gender = "0"
        emotion = "0"

        label_test_file.write("\t".join(
            [wav, dataset, spk_id, gender, emotion, dialect]) + "\n")
        scp_file.write("\t".join([wav, abs_path]) + "\n")


scp_file.close()
label_file.close()
label_test_file.close()
