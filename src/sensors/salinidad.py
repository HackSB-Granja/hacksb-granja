#!/usr/bin/env python

# Simulador de sensor de salinidad.
#
# La salinidad se mide en gramos de sal por litro. Ejemplo:
#
# | Agua dulce | Agua salobre | Agua de mar | Salmuera
# | < 0,05 %   | 0,05 - 3 %   | 3 - 5 %     | > 5 %
# | < 0,5 g/L  | 0,5 - 30 g/L | 30 - 50 g/L | > 50 g/L
#
# Ejecutar:
#    python salinidad [segundos]
#
#    [segundos] OPCIONAL ejecutar script durante n segundos.
#
# Este programa genera valores aleatorios para salinidad de agua # de mar.
# Valores comprendidos entre 3 y 5. Es posible que si el script se ejecuta
# durante mucho tiempo se sobrepasen estos valores.

import json
import math
import os
import random
import sys
import time

# Datos se guardan en 'CSV'.
ROOT = "/var/run/granja"
CSV  = "{:s}/salinidad.csv".format(ROOT)
JSON = "{:s}/salinidad.json".format(ROOT)
TXT = "{:s}/salinidad.txt".format(ROOT)

# Cada 'TICK' segundos, emitir un nuevo valor.
TICK = 3

def usage(code):
    print("Uso: salinidad [segundos]")
    print("")
    print("     [segundos] OPCIONAL Ejecutar script durante n segundos")
    sys.exit(code)

def parse_args():
    if len(sys.argv) > 2:
        usage(1)
    until = -1
    if len(sys.argv) == 2:
        now = time.time()
        until = now + int(sys.argv[1])
    return until

# Valor inicial de salinidad. Valor comprendido entre 5 y 3.
def seed():
    return normalize(random.random(), 5, 3)

# Devuelve un valor entre max y min.
def normalize(val, max, min):
    return val * (max - min) + min

# Incrementa valor.
def increment(val):
    r = random.random()
    increment = normalize(r, 0.075, 0.025)
    if r < 0.20:
        val = val - increment
    if r >= 0.80:
        val = val + increment
    return val

# Crea directorio si no existe.
def ensure_dir(filename):
    if not os.path.exists(filename):
        try:
            os.makedirs(filename, 01777)
        except OSError as e:
            print("Unable to create {:s}: {:s}".format(filename, e.strerror))
    return True

def log(string):
    print(string)

# Programa principal.
def run(until):
    # salinity = seed()
    salinity = 3.80
    now = int(time.time())

    csv = open(CSV, "w")
    log("Escribiendo valores de salinidad en {:s}".format(CSV))
    log("Escribiendo valor actual de salinidad en {:s}".format(JSON))
    while True:
        csv_log(csv, now, salinity)
        json_log(now, salinity)
        time.sleep(TICK)
        salinity = increment(salinity)
        now = int(time.time())
        if until > 0 and until - now <= TICK:
            break
    csv.close()

def csv_log(fd, now, salinity):
    string = "{:d}\t{:.6f}\n".format(now, salinity)
    fd.write(string)
    fd.flush()

def json_log(now, salinity):
    fd = open(JSON, "w")
    data = {'now': now, 'salinity': salinity}
    fd.write(json.dumps(data))
    fd.flush()
    fd.close()

ensure_dir(ROOT)
until = parse_args()
run(until)
