. ./cmd.sh
. ./path.sh
set -e

mfccdir=`pwd`/mfcc
vaddir=`pwd`/vad
nj=24
train_data=`pwd`/data/sparta_train
test_data=`pwd`/data/sparta_test
make_mfcc=`pwd`/exp/make_mfcc
make_vad=`pwd`/exp/make_vad
exp=`pwd`/exp
nnet_dir=`pwd`/exp/xvector_nnet_1a

steps/make_mfcc.sh --nj $nj --cmd "$train_cmd" $train_data $make_mfcc $mfccdir
steps/compute_cmvn_stats.sh  $train_data $make_mfcc $mfccdir

steps/make_mfcc.sh --nj $nj --cmd "$train_cmd" $test_data $make_mfcc $mfccdir
steps/compute_cmvn_stats.sh  $test_data $make_mfcc $mfccdir

sid/compute_vad_decision.sh --nj $nj --cmd "$train_cmd"  $train_data $make_vad $vaddir
sid/compute_vad_decision.sh --nj $nj --cmd "$train_cmd"  $test_data $make_vad $vaddir

sid/nnet3/xvector/extract_xvectors.sh --cmd "$train_cmd" --nj $nj $nnet_dir $train_data $exp/xvectors_train
sid/nnet3/xvector/extract_xvectors.sh --cmd "$train_cmd" --nj $nj $nnet_dir $test_data $exp/xvectors_test
