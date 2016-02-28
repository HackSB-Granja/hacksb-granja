#Sensor examples for everything builtin the board such as 
#Magnometer -> Magnetic pull on device
#Gyroscope - > xyz tilt degree on the device
#Accelerometer -> xyz directional force measurment

from neo import Accel # import accelerometer
from neo import Magno # import magnometer
from neo import Gyro # import gyroscope
from neo import Temp #import libraries
from neo import Barometer

from time import sleep # to add delay

giro = Gyro() # new objects p.s. this will auto initialize the device onboard
acel = Accel()
magno = Magno()
temp = Temp() # init objects p.s. I auto initialize/reset the modules on these calls
baro = Barometer()

acel.calibrate()
giro.calibrate() # Reset current values to 0
magno.calibrate()

def evento(cadena):
    print "Dato: "+cadena

def loguea(cadena):
    print "Dato: "+cadena

while True: # Run forever
    giroVal = giro.get() # Returns a full xyz list [x,y,z] realtime (integers/degrees)
    giroTotal=""
    for i in range(-1, 2):
        giroTotal=giroTotal+","+str(giroVal[i])
        if giroVal[i]>100:
            evento("Alarma de giroscopio, valor {}".format(giroVal[i]))

        loguea ("Giroscopio, valor{}".format(giroTotal))
	aceleraVal = acel.get() #  return xyz of current displacment force
    aceleraTotal=""
    for i in range(-1, 2):
        aceleraTotat=aceleraTotal+","+str(aceleraVal[i])
        if aceleraVal[i]>200:
            evento("Alarma de acelerometro, valor {}".format(aceleraVal[i]))

    loguea ("Acelerometro, valor{}".format(aceleraTotal))
	magnoVal = magno.get() # Above
    magnoTotal=""
    for i in range(-1, 2):
        magnoTotal=magnoTotal+","+str(magnoVal[i])
        if magnoVal[i]>100:
            evento("Alarma de magnetometro, valor {}".format(magnoVal[i]))
        loguea ("Magnetometro, valor{}".format(magnoTotal))
    tempVal = temp.getTemp("c") 
    presionVal = baro.getPressure()
    if tempVal>10:
            evento("Alarma de temperatura, valor {}".format(tempVal))
            evento("Alarma de presion, valor {}".format(presionVal))
    loguea ("Temperatura, valor{}".format(tempVal))
    loguea ("Presion, valor{}".format(presionVal))
    print "----Procesando------" # newline
    sleep(1) # wait a second
