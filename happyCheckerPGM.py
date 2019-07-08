from PIL import Image
import PIL
import glob
import cv2

i=1
for j in range(1,41):
    print(j)
    fnames=glob.glob("/home/alireza/Documents/cv-final-project/orl_faces/s"+str(j)+'/*.pgm')
    print("/home/alireza/Documents/cv-final-project/orl_faces/s"+str(j)+'/*.pgm')
    fnames.sort()

    for fname in fnames:
        print( fname )
        I=cv2.imread(fname,cv2.IMREAD_COLOR)
        cv2.imshow("I",I)
        key=cv2.waitKey(0)

        if key == ord( 'q' ):
            exit(0)
        elif key== ord('a'):
            cv2.imwrite("/home/alireza/Documents/cv-final-project/angry_pgm/"+str(i)+".jpg",I)
            i+=1
        elif key== ord('n'):
            cv2.imwrite("/home/alireza/Documents/cv-final-project/neutral_pgm/"+str(i)+".jpg",I)
            i+=1

cv2.destroyAllWindows()