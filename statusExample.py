#!/usr/bin/python

import json
import time
from arduino import arduinoSerial

arduino = arduinoSerial()

data = {}
receivedData = ""

while( True ):
   data['light'] = 'on'
   arduino.write(json.dumps(data))

   object = json.loads(arduino.read())
   print object["light"]

   time.sleep(1)

   data['light'] = 'off'
   arduino.write(json.dumps(data))

   object = json.loads(arduino.read())
   print object["light"]

   time.sleep(1)

