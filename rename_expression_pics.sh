#! /bin/bash
 
cd /home/alireza/Documents/cv-final-project/KDEF_and_AKDEF/KDEF &&

for i in {1..140} 
do
	cd file-$i &&
	ls | cat -n | while read n f; do mv "$f" "file-$n.jpg"; done &&
	cd ../ &&
done
