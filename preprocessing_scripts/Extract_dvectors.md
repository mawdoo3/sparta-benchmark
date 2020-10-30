# Extract Dvectors 
This documents present the steps extract dvectors for speech.

## prerequisite

* Python 3.6 or 3.7 is needed.
* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.0.1).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).

## Steps

* Clone Real-time Voice Cloning directory
```bash
git clone https://github.com/CorentinJ/Real-Time-Voice-Cloning.git
```

* Create wav.scp file; which is the ID of the utterance and its path as following:

```
wav_1.wav path/to/wav_1.wav
wav_2.wav path/to/wav_2.wav
```

A [tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/training-acoustic-models.html#create-files-for-datatrain) for the creation of this file.

* Run the "extract_dvectors.py" (included in this directory) script which takes 2 arguments:
```bash
extract_dvectors.py <wav.scp path> <output pickle name>
```

