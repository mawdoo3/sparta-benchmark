import os

path = '/data/ksu_emotions/data/SPEECH/'
class_emotions = {'E00': 'neutral', 'E01': 'happiness', 'E02': 'sadness', 'E03': 'surprise',
                  'E04': 'questioning', 'E05': 'anger'}


label_file = open("labels.txt", "w")
scp_file = open("wav.scp", "w")
dataset = "ksu"

for phase in os.listdir(path):
    if os.path.isdir(os.path.join(path, phase)):
        for emotion_path in os.listdir(os.path.join(path, phase)):
            for audio_file in os.listdir(os.path.join(path, phase, emotion_path)):
                if '.wav' in audio_file:
                    abs_path = os.path.abspath(os.path.join(phase, emotion_path, audio_file))
                    spk_id = dataset + "-" + audio_file.split("P")[1].split("S")[0]
                    gender = "male" if "P0" in audio_file else "female"
                    emotion = str(0)
                    dialect = str(0)
                    for key in class_emotions:
                        if key in audio_file:
                            emotion = class_emotions[key]

                    label_file.write("\t".join(
                        [audio_file, dataset, spk_id, gender, emotion, dialect]) + "\n")
                    scp_file.write("\t".join([audio_file, abs_path]) + "\n")


label_file.close()
scp_file.close()
