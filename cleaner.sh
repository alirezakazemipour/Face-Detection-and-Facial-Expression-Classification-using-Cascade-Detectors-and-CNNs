#! /bin/bash

for i in {37..39}
do

cd /home/alireza/Documents/cv-final-project/CroppedYale/yaleB$i &&
sudo rm WS_FTP.LOG &&
sudo rm yaleB${i}_P00.info && 
ls | cat -n | while read n f; do mv "$f" "file-$n.pgm"; done
ls
done


#ls -l | grep ^- | wc -l show no. of files in a folder
#ls | cat -n | while read n f; do mv "$f" "$(($n+$d)).jpg"; done

