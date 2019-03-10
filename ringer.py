#!/usr/bin/env python3
import RPi.GPIO as gpio
import time
from subprocess import Popen
 
soundfile = '/home/pi/sounds/guten_abend.wav'

def setup(right,left,hs):
    gpio.cleanup()
    gpio.setmode(gpio.BCM)
    gpio.setup(left, gpio.OUT)
    gpio.setup(right, gpio.OUT)
    gpio.output(right, gpio.LOW)
    gpio.output(left, gpio.LOW)


def pwm(right,left):
    p1 = gpio.PWM(right, 50)
    p2 = gpio.PWM(left, 50)
    return (p1,p2)

def stop(p1,p2):
    p1.stop()
    p2.stop()

def ring(p1,p2,hs):
    print(hs)
    p1.start(0)
    p2.start(0)
    gpio.setup(hs, gpio.IN)
    gpio.input(hs)

    try:
      while gpio.input(hs):
            p1.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(50)
            p1.ChangeFrequency(50)
            p2.ChangeFrequency(50)
            time.sleep(1)
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            time.sleep(3)
            p1.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(50)
            if gpio.input(hs) == gpio.LOW:
                stop(p1,p2)
                gpio.cleanup()
                time.sleep(2)
                Popen(["/usr/bin/aplay", soundfile])
                return
    except KeyboardInterrupt:
        pass
    stop(p1,p2)
    gpio.cleanup()
