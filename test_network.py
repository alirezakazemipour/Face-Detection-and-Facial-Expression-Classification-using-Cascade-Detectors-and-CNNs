# USAGE
# python test_network.py --model santa_not_santa.model --image images/examples/santa_01.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

cap = cv2.VideoCapture(0)
# load the trained convolutional neural network
print( "[INFO] loading network..." )
model = load_model( "happy_not_happy.model" )
face_detector = cv2.CascadeClassifier( '/home/alireza/Documents/cv-final-project/lbp/cascade.xml' )
k=0

im_w=28#28
im_h=28#28


while True:

	ret, I = cap.read()
	orig = I.copy()

	gray = cv2.cvtColor( I, cv2.COLOR_BGR2GRAY )
	gray = cv2.equalizeHist( gray )
	faces = face_detector.detectMultiScale( gray, 1.1, 3, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(30, 30) )
	if len( faces ) != 0:
		faces[:, 2:] += faces[:, :2]
	for x1, y1, x2, y2 in faces:
		cv2.rectangle( I, (x1, y1), (x2, y2), (0, 255, 0), 2 )
		# cv2.imshow("I",I)
		image = orig[y1:y2, x1:x2]

	# pre-process the image for classification
		image = cv2.resize( image, (im_w, im_h) )
		cv2.imshow("image",image)
		image = image.astype( "float" ) / 255.0
		image = img_to_array( image )
		image = np.expand_dims( image, axis=0 )

	# classify the input image

	predictions = model.predict(image)
	print(np.argmax(predictions[0]))
	(happy, angry, neutral) = model.predict( image )[0]

	# build the label
	if happy >= neutral and happy >= angry:
		label = "happy"
		proba = happy

	elif angry >= neutral and happy < angry:
		label = "angry"
		proba = angry

	elif angry < neutral and neutral > happy:
		label = "neutral"
		proba = neutral

	# label = "{}: {:.2f}%".format(label, proba * 100)

	# draw the label on the image
	output = imutils.resize(orig, width=400)
	cv2.putText(I, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
				0.7, (0, 255, 0), 2)

	# show the output image
	cv2.imshow("I", I)
	cv2.waitKey(2)