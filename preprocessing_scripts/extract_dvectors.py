from sklearn.metrics.pairwise import cosine_similarity
from itertools import combinations
import numpy as np
from encoder.inference import *
from encoder.audio import *
import pickle
from tqdm import tqdm
import sys
files = [i.strip() for i in open(sys.argv[1])]
load_model('/code/Real-Time-Voice-Cloning/encoder/pretrained.pt')
db = open(sys.argv[2], "wb")
d = {}
errors = []
for i in tqdm(files):
    try:
        audio = preprocess_wav(i.split()[1].strip())
        embeds = embed_utterance(audio)
        d[i.split()[0]] = embeds
    except:
        errors.append(i)

for i in errors:
    error_file = "errors_{}".format(sys.argv[2])
    with open(error_file, "w+") as f:
        for i in errors:
            f.write("{}\n".format(i))
    print("Some files had problems\n please check {}".format(error_file))

pickle.dump(d, db)
db.close()

