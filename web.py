#!/usr/bin/env python3
from flask import Flask, render_template
import RPi.GPIO as gpio
import ringer, dialer
import threading
from subprocess import Popen

app = Flask(__name__, static_url_path='/static')    

right = 12
left = 13
handset = 7
rotary = 15

 
@app.route('/')
def index():
    return render_template('ringer.html')

@app.route('/ring/')
def ring():
    ringer.setup(right,left,handset)
    p1,p2 = ringer.pwm(right,left) 
    ringer.ring(p1,p2,handset)
    return index()

@app.route('/ring/stop/')
def stop():
  ringer.stop(p1,p2)

if __name__ == '__main__':
    web = app.run(host='0.0.0.0', port=80)
