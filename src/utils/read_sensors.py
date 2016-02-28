#!/usr/bin/python
import os
import time

import json
import cv2

from lib.neo.Neo import Accel, Gyro, Magno

root = os.environ['PYTHONPATH']
data_path = root + '/data/'
www_data = root + '/www/data/'
salinidad_path = '/var/run/granja/salinidad.json'
panel_json = www_data + 'panel.json'

data = dict()

accel = Accel()
gyro = Gyro()
magno = Magno()

accel.calibrate()
gyro.calibrate()
magno.calibrate()

while True:
    x, y ,z = accel.get()
    data['accelerometer'] = {'x': float(x), 'y': float(y), 'z': float(z)} 

    xg, yg, zg = gyro.get()
    data['gyroscope'] = {'x': float(xg), 'y': float(yg), 'z': float(zg)}
        
    xm, ym, zm = magno.get()
    data['magnometer'] = {'x': float(xm), 'y': float(ym), 'z': float(zm)}


    # Capture frame
    frame = cv2.imread(data_path + 'images/last_camera_reading', 0)

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
        data['net_monitor'] = {'status': 'ko', 'picture': 'data/last_camera_reading.jpg'} # TODO: Log data when KO
    else:
        data['net_monitor'] = {'status': 'ok', 'picture': 'data/last_camera_reading.jpg'} # TODO: Log data when OK

    # Salinidad
    with open(salinidad_path, 'r') as fd:
        salinidad_data = json.load(fd)
        data['salinity'] = {'value': salinidad_data['salinity']}

    with open(panel_json, 'w') as fd:
        fd.write(json.dumps(data))

    print('Waiting...')
    time.sleep(2.5)
    print('Reading current values...')
