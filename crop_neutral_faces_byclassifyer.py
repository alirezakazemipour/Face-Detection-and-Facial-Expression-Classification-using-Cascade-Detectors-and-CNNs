from PIL import Image
import PIL
import glob
import cv2
i=0
k=0
face_detector = cv2.CascadeClassifier( '/home/alireza/Documents/cv-final-project/lbp/cascade.xml' )

fnames=glob.glob("/home/alireza/Documents/cv-final-project/angry/*.jpg")
fnames.sort()

for fname in fnames:
    I=cv2.imread(fname,cv2.IMREAD_COLOR)
    R=I.copy()
    gray= cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    gray=cv2.equalizeHist(gray)
    faces = face_detector.detectMultiScale(gray,1.1,3,flags=cv2.CASCADE_SCALE_IMAGE,minSize=(30,30))
    if len(faces) != 0:
        faces[:,2:] += faces[:,:2]
    for x1, y1, x2, y2 in faces:
            # cv2.rectangle(I, (x1, y1), (x2, y2), (0,255,0), 2)

            J=R[y1:y2,x1:x2]
            cv2.imwrite("/home/alireza/Documents/cv-final-project/croppedAngry/"+str(i)+".jpg",J)
            i+=1

cv2.destroyAllWindows()