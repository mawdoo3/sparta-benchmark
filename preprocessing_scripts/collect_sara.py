import os
import re

path = '/data/asr-data/speech_profiling_data/dialect_detection/SARA/'

label_file = open("labels.txt", "w")
scp_file = open("wav.scp", "w")
dataset = "sara"

for dialect_path in os.listdir(path):
    if os.path.isdir(os.path.join(path, dialect_path)):
        for dur in os.listdir(os.path.join(path, dialect_path)):
            for wav in os.listdir(os.path.join(path, dialect_path, dur)):
                utt_id = '-'.join([dur, wav])
                abs_path = os.path.join(path, dialect_path, dur, wav)
                spk_id = re.split('F|M', wav)[0]
                if "M" in wav:
                    spk_id = dataset + "-M" + spk_id
                    gender = "male"
                else:
                    spk_id = dataset + "-F" + spk_id
                    gender = "female"

                dialect = wav[:3].lower()
                if dialect == "arp":
                    dialect = "glf"
                emotion = "0"
                label_file.write("\t".join(
                    [utt_id, dataset, spk_id, gender, emotion, dialect]) + "\n")
                scp_file.write("\t".join([utt_id, abs_path]) + "\n")

label_file.close()
scp_file.close()
