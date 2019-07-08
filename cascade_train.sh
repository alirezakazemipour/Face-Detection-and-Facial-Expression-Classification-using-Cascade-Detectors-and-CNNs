#! /bin/bash
cd ..
find ./negativeSamples -iname "*.jpg" > negatives.txt &&
find ./positiveSamples -iname "*.jpg" > positives.txt &&
perl bin/createsamples.pl positives.txt negatives.txt samples 5000 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 40 -h 40"&&
python mergevec.py -v samples/ -o samples.vec &&
num_of_neg_samples=3254 &&
opencv_traincascade -data lbp -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 2201 -numNeg $num_of_neg_samples -w 40 -h 40 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024 -featureType LBP
