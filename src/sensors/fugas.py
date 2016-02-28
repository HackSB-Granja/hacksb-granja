#!/usr/bin/env python
import time
import os

import cv2

root = os.environ['PYTHONPATH']
data_path = root + 'data/'

while(True):
    # Capture frame
    frame = cv2.imread(data_path + 'images/last_camera_reading', 0)
    #frame = cv2.imread('negative_images/negative.jpg', 0)

    # Use xml trained classifier
    cascPath = data_path + 'fugas/cascade.xml'
    netCascade = cv2.CascadeClassifier(cascPath)

    # Process image and get matches
    nets = netCascade.detectMultiScale(
        frame,
        scaleFactor = 1.2,
        minNeighbors=2200,
    )

    # Log image processing result
    if len(nets):
        print('ko') # TODO: Log data when KO
    else:
        print('ok') # TODO: Log data when OK

    # Read values every 5 seconds
    time.sleep(5)
