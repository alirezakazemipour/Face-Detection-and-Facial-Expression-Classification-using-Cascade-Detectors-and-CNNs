#! /bin/bash

cd /home/alireza/Documents/cv-final-project/KDEF_and_AKDEF/KDEF &&
j=1 &&
for i in {1..62} 
do
	cd file-$i &&
	cp file-12.jpg /home/alireza/Desktop/happy/$j.jpg &&
	cd ../ &&
	((j++ ))
done
for i in {63..140} 
do
	cd file-$i &&
	cp file-20.jpg /home/alireza/Desktop/happy/$j.jpg &&
	cd ../ &&
	((j++ ))
done