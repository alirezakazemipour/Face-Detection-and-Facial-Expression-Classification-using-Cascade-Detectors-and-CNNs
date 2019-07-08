import numpy as np
import cv2

# https://github.com/opencv/opencv/blob/master/data/lbpcascades/lbpcascade_frontalface_improved.xml
face_detector = cv2.CascadeClassifier( '/home/alireza/Documents/cv-final-project/Face-Detection-and-Facial-Expression-Classification-using-Cascade-Detectors-and-Convolutional-Neural/lbp/cascade.xml' )
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml
smile_detector = cv2.CascadeClassifier( '/home/alireza/Documents/cv-lab14/smile.xml' )

cap = cv2.VideoCapture( 0 )

while 1:
    ret, I = cap.read()

    # complete the code here in order to detect your face and your smile
    gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_detector.detectMultiScale(I,1.1,3,flags=cv2.CASCADE_SCALE_IMAGE,minSize=(30,30))

    # print("faces shapes",faces[0])

    if len(faces) != 0:
        faces[:,2:] += faces[:,:2]
    for x1, y1, x2, y2 in faces:
        cv2.rectangle(I, (x1, y1), (x2, y2), (0,255,0), 2)

        J=I[y1:y2 , x1:x2]
        smiles = smile_detector.detectMultiScale(J,1.1,3,flags=cv2.CASCADE_SCALE_IMAGE,minSize=(30,30))
        if len( smiles ) != 0:
            smiles[:, 2:] += smiles[:, :2]
        for x1, y1, x2, y2 in smiles:
            cv2.rectangle( J, (x1, y1), (x2, y2), (0, 0, 255), 2 )

    cv2.imshow( 'I', I )
    key = cv2.waitKey( 60 )
    if key == ord( 'q' ):
        break

cap.release()
cv2.destroyAllWindows()