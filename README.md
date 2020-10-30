# SPARTA-benchmark

SPARTA stands for Speech Profiling for ARabic TAlk. The purpose of this project is to identify the speaker’s gender, dialect, and emotion when speaking from a given utterance. 

This research profiles the speaker based on their voice. From a given speech, our model predicts gender, emotion, and dialect in real-time.

- Emotion [Sad, Happy, Angry, Surprise, Questioning, and Neutral].
- Gender [Male and Female] in the Arabic language (as many other languages).
- Dialect [Egypt, MSA, Levant, Gulf, North Africa].


## Datasets

1. Qatar Computing Research Institute [QCRI](https://github.com/qcri/dialectID)
2. King Saud University Emotions [KSUEmotions](https://catalog.ldc.upenn.edu/LDC2017S12)
3. Arabic Natural Audio Dataset [ANAD](https://data.mendeley.com/datasets/xm232yxf7t/1)
4. Spoken Arabic Regional Archive [SARA](https://data.mendeley.com/datasets/btfx5pw2rm/2)
5. King Saud University Arabic Speech Database [KSU](https://catalog.ldc.upenn.edu/LDC2014S02)
6. Multi Dialect Arabic Speech [MDAS](http://almeman.weebly.com/arabic-speech-corpora.html)

## Data Preprocessing


To reproduce the dataset collected please follow the instructions:
1. Download Datasets from the links above.
2. Run `collect_DATASETNAME.py` for all datasets.
3. Make the Train/Dev/Test split by running the `preprocessing_scripts/split.py`
4. Extract features by running `extract_FEATURENAME.py` for all features
