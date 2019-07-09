from PIL import Image
import PIL
import glob
import cv2
import numpy as np

i=1770

fnames=glob.glob("/home/alireza/Documents/cv-final-project/Face-Detection-and-Facial-Expression-Classification-using-Cascade-Detectors-and-Convolutional-Neural/images/neutral/*.jpg")

fnames.sort()

for fname in fnames:
    print( fname )
    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    # I=cv2.flip(I,1)
    # M = cv2.getRotationMatrix2D( (I.shape[0] / 2, I.shape[1] / 2), 30, 1 )
    # I = cv2.warpAffine( I, M, (I.shape[0], I.shape[1]) )
    # cv2.add(I,100,I)
    mean = 0
    var = 0.8
    sigma = var ** 0.5
    gauss = np.random.normal( mean, sigma, (I.shape[0], I.shape[1], 3) )
    gauss = gauss.reshape( I.shape)
    I=I+gauss
    cv2.imwrite("/home/alireza/Documents/cv-final-project/croppedNeutral/"+str(i)+".jpg",I)
    i+=1

cv2.destroyAllWindows()