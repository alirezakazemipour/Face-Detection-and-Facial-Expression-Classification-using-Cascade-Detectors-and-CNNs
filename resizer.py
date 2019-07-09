from PIL import Image
import PIL
import glob
import cv2

i=3353

fnames=glob.glob("/home/alireza/Documents/cv-final-project/falsePositives/*.jpg")

fnames.sort()

for fname in fnames:
    print( fname )
    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    # I=cv2.resize(I,(168,192))
    cv2.imwrite("/home/alireza/Documents/cv-final-project/negativeSamples/"+str(i)+".jpg",I)
    i+=1

cv2.destroyAllWindows()