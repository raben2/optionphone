#!/usr/bin/env python3
import RPi.GPIO as gpio
import time, re
from subprocess import Popen, call
from collections import defaultdict

soundfile = '/home/pi/sounds/line.wav'

def play(pin):
   Popen(["/usr/bin/aplay", soundfile])

def playback(line):
  try: 
    digit, file = line.split(",")
    soundfile = '/home/pi/sounds/%s' % file
    call("/usr/bin/aplay " + soundfile, shell=True)
  finally:
    dialed = ''
    return dialed
  

columns = defaultdict(list)
handset = 7
rotary = 17
gpio.setmode(gpio.BCM)
gpio.setup(handset, gpio.IN)
gpio.input(handset)
gpio.setup(rotary, gpio.IN, pull_up_down=gpio.PUD_UP) 
gpio.add_event_detect(handset,gpio.FALLING)
gpio.add_event_callback(handset,play)
num = 0
prnt = 0
last = 0    
dialed = ''

while True:
  
  dialer = gpio.input(rotary)    
  if (dialer == 1) and (dialer != last):
        last = 1
        prnt = 1
        num += 1
        time.sleep(0.05)
        continue    

  if (dialer == 0) and (dialer != last):
        last = 0
        time.sleep(0.05)
        continue    

  if (dialer == 0) and (dialer == last):
      if (prnt == 1):
        if (num == 10):
            num = 0 

        if (num == 0):
            dialed = '%s0' % dialed
             
        if (num == 1):
            dialed = '%s1' % dialed
                            
        if (num == 2):
            dialed = '%s2' % dialed
             
        if (num == 3):
            dialed = '%s3' % dialed
             
        if (num == 4): 
            dialed = '%s4' % dialed
                         
        if (num == 5): 
            dialed = '%s5' % dialed
                         
        if (num == 6): 
            dialed = '%s6' % dialed
                          
        if (num == 7):
            dialed = '%s7' % dialed
                          
        if (num == 8):  
            dialed = '%s8' % dialed
                          
        if (num == 9): 
            dialed = '%s9' % dialed
             
        if len(dialed)  == 4:
            print(dialed)
            with open("/home/pi/telephonebook.txt", "r") as f:
                for line in f.readlines():
                   if re.search(dialed, line):
                      playback(line)
                      f.close()
                      continue  
                   else:
                     f.close()
                     continue
        if len(dialed) > 4:
            dialed = ''
            continue           
        num = 0
        prnt = 0
        last = 0
  continue    