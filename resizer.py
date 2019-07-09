from PIL import Image
import PIL
import glob
import cv2

i=3101

fnames=glob.glob("/home/alireza/Desktop/croppedAngry/*.jpg")

fnames.sort()

for fname in fnames:
    print( fname )
    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    I=cv2.resize(I,(168,192))
    cv2.imwrite("/home/alireza/Desktop/positiveSamples/"+str(i)+".jpg",I)
    i+=1

cv2.destroyAllWindows()