# Extract xvectors 
This documents present the steps to extract vectors for speech.

## prerequisite

* kaldi ([Install](https://www.eleanorchodroff.com/tutorial/kaldi/installation.html))
* Cuda

## Steps

* Clone kaldi directory
```bash
git clone https://github.com/kaldi-asr/kaldi.git kaldi --origin upstream
```

* Download a pre-trained xvector model and extract in egs directory [Model](https://kaldi-asr.org/models/m3)

* Link the following directories from any other example and create data directory
```bash
cd mode_directory
ln -s ../wsj/s5/steps .
ln -s ../wsj/s5/utils .
ln -s ../../src .
ln -s ../../sid .
                    
cp ../wsj/s5/path.sh .
cp ../wsj/s5/cmd.sh .

mkdir data/train
mkdir data/test
```
Note: edit path of kaldi in path.sh if necessary.

* Create kaldi files for training; [A step by step tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/training-acoustic-models.html#create-files-for-datatrain)

* Execute the script in preprocessing steps
