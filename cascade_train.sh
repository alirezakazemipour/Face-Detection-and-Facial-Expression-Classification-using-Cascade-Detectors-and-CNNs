#! /bin/bash
cd ..
find ./negativeSamples -iname "*.jpg" > negatives.txt &&
find ./positiveSamples -iname "*.jpg" > positives.txt &&
perl bin/createsamples.pl positives.txt negatives.txt samples 5000 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 40 -h 40"&&
python mergevec.py -v samples/ -o samples.vec &&
opencv_traincascade -data lbp -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 3277 -numNeg 3352 -w 40 -h 40 -mode ALL -precalcValBufSize 2048 -precalcIdxBufSize 2048 -featureType LBP
