import os

path = '/data/asr-data/acoustic/gen_clean/king_saud/'

genders = []

with open(os.path.join(path, 'spk2gender'),'r') as f:
    genders = f.readlines()

genders = [i.strip() for i in genders]

genders_dict = dict()
for g in genders:
    temp = g.split()
    if temp[1] == "m":
        gender = "male"
    else:
        gender = "female"
    genders_dict[temp[0]] = gender

paths = []
with open(os.path.join(path, 'wav.scp'),'r') as f:
    paths = f.readlines()

paths = [i.strip() for i in paths]
paths_dict = dict()

for i in paths:
    temp = i.split()
    paths_dict[temp[0]] = temp[1]

waves = []

with open(os.path.join(path, 'SPARTA'),'r') as f:
    waves = f.readlines()

waves = [i.strip() for i in waves]

output_gender = []
output_path = []
speakers = []

for wav in waves:
    output_path.append(paths_dict[wav])
    temp = wav.split('_')
    speakers.append("king-"+temp[0])
    output_gender.append(genders_dict[temp[0]])

with open('sparta.scp', 'w') as f:
    for item1, item2 in zip(waves, output_path):
        f.write('{}\t{}\n'.format(item1, item2))

with open('labels.txt', 'w') as f:
    for wav, speaker, gender in zip(waves, speakers, output_gender):
        f.write('{}\tking\t{}\t{}\t0\t0\n'.format(wav, speaker, gender))
