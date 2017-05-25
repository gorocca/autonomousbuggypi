# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import urllib
import imutils
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--images", required=True, help="path to images directory")
#args = vars(ap.parse_args())

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# loop over the image paths
#imagePaths = list(paths.list_images(args["images"]))
#cam = cv2.VideoCapture(0)

#for imagePath in imagePaths:   




while True:

   
   stream=urllib.urlopen('http://@192.168.0.1:8080/?action=stream/frame.mjpg')
   bytes=''
   imagenCompleta = False
   while not imagenCompleta:
       bytes+=stream.read(1024)
       a = bytes.find('\xff\xd8')
       b = bytes.find('\xff\xd9')
       if a!=-1 and b!=-1:
           jpg = bytes[a:b+2]
           bytes= bytes[b+2:]
           image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
           cv2.imshow('i',image)
           imagenCompleta = True

   image = imutils.resize(image, width=min(400, image.shape[1]))
   orig = image.copy()
   (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)
   for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

   rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
   pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
   for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
   print("[INFO] {}: {} original boxes, {} after suppression".format(
		"Imagen", len(rects), len(pick)))

   cv2.imshow("Before NMS", orig)
   cv2.imshow("After NMS", image)
   cv2.waitKey(1)
