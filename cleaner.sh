#! /bin/bash
cd /home/alireza/Documents/cv-final-project/CroppedYale/yaleB03
sudo rm WS_FTP.LOG 
sudo rm yaleB02_P00.info 
ls | cat -n | while read n f; do mv "$f" "file-$n.pgm"; done
ls

