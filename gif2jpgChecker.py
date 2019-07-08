from PIL import Image
import PIL
import glob
import cv2
import matplotlib.pyplot as plt

i=1
fnames=glob.glob("/home/alireza/Documents/cv-final-project/nottingham_originals/*.gif")
fnames.sort()
print(len(fnames))

for fname in fnames:
    im=Image.open(fname)
    im=im.convert('RGB')
    # im=im.resize( (168,192), PIL.Image.ANTIALIAS )
    im.save("/home/alireza/Documents/cv-final-project/happyChecker/"+str(i)+".jpg")
    print(im.size)
    i+=1
