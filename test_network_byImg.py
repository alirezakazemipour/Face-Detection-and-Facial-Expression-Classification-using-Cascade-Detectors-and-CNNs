# USAGE
# python test_network.py --model santa_not_santa.model --image images/examples/santa_01.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import glob
import imutils
import cv2

# load the trained convolutional neural network
print( "[INFO] loading network..." )
model = load_model( "happy_not_happy.model" )

fnames=glob.glob("/home/alireza/Documents/cv-final-project/positiveSamples/*.jpg")
fnames.sort()

for fname in fnames:

    fname='/home/alireza/Desktop/smile2.jpeg'
    image=cv2.imread(fname)
    # load the image
    # image = cv2.imread(args["image"])
    orig = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)



    # classify the input image
    (not_happy, happy) = model.predict(image)[0]

    # build the label
    label = "happy" if happy > not_happy else "not_happy"
    proba = happy if happy > not_happy else not_happy
    label = "{}: {:.2f}%".format(label, proba * 100)

    # draw the label on the image
    output = imutils.resize(orig, width=400)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
        0.7, (0, 255, 0), 2)

    # show the output image
    cv2.imshow("Output", output)
    cv2.waitKey(0)