#! /bin/bash

cd /home/alireza/Documents/cv-final-project/KDEF_and_AKDEF/KDEF &&
j=1 &&
for i in {1..62}
do
	cd file-$i &&
	cp file-11.jpg /home/alireza/Desktop/angry/$j.jpg &&
	cd ../ &&
	((j++ ))
done
for i in {64..140}
do
	cd file-$i &&
	cp file-10.jpg /home/alireza/Desktop/angry/$j.jpg &&
	cd ../ &&
	((j++ ))
done

	cd file-63 &&
	cp file-12.jpg /home/alireza/Desktop/angry/$j.jpg