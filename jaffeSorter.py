from PIL import Image
import PIL
import glob
import cv2

i=143
fnames=glob.glob("/home/alireza/Documents/cv-final-project/jaffedbase/jaffe/*.tiff")
fnames.sort()

for fname in fnames:

    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    cv2.imshow("I",I)
    key=cv2.waitKey(0)

    if key == ord( 'q' ):
             exit(0)
    elif key== ord('s'):
            cv2.imwrite("/home/alireza/Documents/cv-final-project/angry/"+str(i)+".jpg",I)
            i+=1

cv2.destroyAllWindows()