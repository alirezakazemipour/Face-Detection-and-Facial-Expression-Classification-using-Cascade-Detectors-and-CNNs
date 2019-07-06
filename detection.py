from PIL import Image
import PIL
import glob
import cv2

face_detector = cv2.CascadeClassifier( '/home/alireza/Documents/cv-final-project/lbp/cascade.xml' )

fnames=glob.glob("/home/alireza/Documents/cv-final-project/ExtendedYaleB/yaleB13/*.pgm")
fnames.sort()

for fname in fnames:
    print(fname)
    I=cv2.imread(fname,cv2.COLOR_BGR2GRAY)
    I=cv2.equalizeHist(I)

    faces = face_detector.detectMultiScale(I,1.1,3,flags=cv2.CASCADE_SCALE_IMAGE,minSize=(30,30))
    if len(faces) != 0:
        faces[:,2:] += faces[:,:2]
    for x1, y1, x2, y2 in faces:
        cv2.rectangle(I, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow( 'I', I )
    key = cv2.waitKey( 0 )
    if key == ord( 'q' ):
        break
    elif key== ord(s):


cv2.destroyAllWindows()