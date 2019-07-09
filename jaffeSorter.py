from PIL import Image
import PIL
import glob
import cv2

i=143
fnames=glob.glob("/home/alireza/Documents/cv-final-project/utrecht/*.jpg")
fnames.sort()

for fname in fnames:

    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    cv2.imshow("I",I)
    key=cv2.waitKey(0)

    if key == ord( 'q' ):
             exit(0)
    elif key== ord('s'):
            I = cv2.resize( I, (168, 192) )
            cv2.imwrite("/home/alireza/Documents/cv-final-project/falsePositives/"+str(i)+".jpg",I)
            i+=1

cv2.destroyAllWindows()