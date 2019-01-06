#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIGGER = 12
ECHO    = 6
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIGGER,False)

while True:
    GPIO.output(TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER,False)
    start = time.time()
    while GPIO.input(ECHO)==0:
        start = time.time()
    while GPIO.input(ECHO)==1:
        stop = time.time()
    tiempo = stop-start
    distancia = (tiempo * 34300)/2
    print distancia
    time.sleep(1)
