import os

path = '/data/asr-data/speech_profiling_data/emotion_detection/Arabic_natural_audio/output'
class_emotions = {'v1': 'happiness', 'v2': 'surprise', 'v3': 'happiness', 'v4': 'anger',
        'v5': 'anger', 'v6': 'surprise', 'v7': 'anger','v8': 'happiness'}

label_file = open("labels.txt", "w")
scp_file = open("wav.scp", "w")
dataset = "anad"

for wav in os.listdir(path):
    abs_path = os.path.join(path, wav)
    spk_id = dataset + "-" + '-'.join(wav.split("-")[:2])
    gender = "0"
    emotion = class_emotions[wav[:2].lower()]
    dialect = "0"
    
    label_file.write("\t".join(
        [wav, dataset, spk_id, gender, emotion, dialect]) + "\n")
    scp_file.write("\t".join([wav, abs_path]) + "\n")


label_file.close()
scp_file.close()
