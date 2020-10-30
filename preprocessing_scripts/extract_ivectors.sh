. ./cmd.sh
. ./path.sh
set -e

mfccdir=`pwd`/mfcc
vaddir=`pwd`/vad
nj=24
num_threads=4
ivectors_dim=400
train_data=`pwd`/data/sparta_train
test_data=`pwd`/data/sparta_test
make_mfcc=`pwd`/exp/make_mfcc
make_vad=`pwd`/exp/make_vad
exp=`pwd`/exp

steps/make_mfcc.sh --nj $nj --cmd "$train_cmd" $train_data $make_mfcc $mfccdir
steps/compute_cmvn_stats.sh  $train_data $make_mfcc $mfccdir

steps/make_mfcc.sh --nj $nj --cmd "$train_cmd" $test_data $make_mfcc $mfccdir
steps/compute_cmvn_stats.sh  $test_data $make_mfcc $mfccdir

sid/compute_vad_decision.sh --nj $nj --cmd "$train_cmd"  $train_data $make_vad $vaddir
sid/compute_vad_decision.sh --nj $nj --cmd "$train_cmd"  $test_data $make_vad $vaddir

sid/train_diag_ubm.sh --cmd "$train_cmd --mem 16G" --nj $nj --num-threads $num_threads $train_data 2048 $exp/diag_ubm
sid/train_full_ubm.sh --cmd "$train_cmd --mem 32G" --nj $nj --remove-low-count-gaussians false $train_data $exp/diag_ubm $exp/full_ubm
sid/train_ivector_extractor.sh --cmd "$train_cmd --mem 32G" --ivector-dim $ivectors_threads --num-iters 5 $exp/full_ubm/final.ubm $train_data $exp/extractor

sid/extract_ivectors.sh --cmd "$train_cmd --mem 32G" --nj $nj $exp/extractor $train_data $exp/ivectors_train
sid/extract_ivectors.sh --cmd "$train_cmd --mem 32G" --nj $nj $exp/extractor $test_data $exp/ivectors_test
