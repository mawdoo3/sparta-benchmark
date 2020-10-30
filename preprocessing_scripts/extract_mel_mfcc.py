import os
import pickle

import argparse
import yaml
import librosa
from tqdm import tqdm

root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)


def preprocess_features(config_path):
    hparams = {}
    with open(os.path.join(root_path, config_path)) as f:
        hparams = yaml.load(f, Loader=yaml.FullLoader)

    mel_dataset = {}
    mfcc_dataset = {}
    mel_filename = os.path.join(root_path, hparams["data_dir"], "{}.pickle".format("mel"))
    mfcc_filename = os.path.join(root_path, hparams["data_dir"], "{}.pickle".format("mfcc"))
    hop_length = int(hparams['sample_rate'] * hparams['frame_shift'])
    win_length = int(hparams['sample_rate'] * hparams['frame_duration'])
    with open(os.path.join(root_path, hparams['data_dir'], hparams['scp_file'])) as f:
        lines = f.readlines()
        for line in tqdm(lines):
            utt_id, path = line.strip().split()
            y, sr = librosa.load(path)
            if len(y) < hparams['n_fft']:
                print("Audio {} is too short: {}".format(utt_id, path))
                continue

            mel_signal = librosa.feature.melspectrogram(
                y=y, sr=sr, S=None, n_fft=hparams['n_fft'], hop_length=hop_length,
                win_length=win_length, window='hann', center=hparams['mel_center'],
                pad_mode='reflect', power=hparams['power'], n_mels=hparams['n_mels'],
                fmax=hparams['f_max'], fmin=hparams['f_min'])
            mfcc_signal = librosa.feature.mfcc(S=mel_signal, n_mfcc=hparams['n_mfcc'])

            mel_signal = librosa.util.normalize(mel_signal)
            mfcc_signal = librosa.util.normalize(mfcc_signal)
            mel_dataset[utt_id] = mel_signal
            mfcc_dataset[utt_id] = mfcc_signal

    pickle.dump(mel_dataset, open(mel_filename, "wb"))
    pickle.dump(mfcc_dataset, open(mfcc_filename, "wb"))


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-c", "--config", type=str, default='config.yml',
                             help="Experiment Configurations ")
    run_args = args_parser.parse_args()

    preprocess_features(run_args.config)
