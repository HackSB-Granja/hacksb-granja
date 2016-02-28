#!/usr/bin/python
import json

root = '../../www/data/'
panel_json = root + 'panel.json'

data = dict()

# with open('/sys/class/misc/FreescaleAccelerometer/data', 'r') as fd:
with open('/home/peibolvig/data', 'r') as fd:
    accelerometer = fd.readline()
    x, y ,z = list(accelerometer.rstrip().split(','))
    data['accelerometer'] = {'x': float(x), 'y': float(y), 'z': float(z)} 

    
with open(panel_json, 'w') as fd:
    fd.write(json.dumps(data))
