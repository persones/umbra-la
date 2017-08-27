import sys
import os.path
from time import sleep, strftime
import si7021
import tsl2561
import mpl3115a2
import timesensor

logname = "/var/logger.csv"
sys.path.append("/home/person/code/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD/")

from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD()  

def displaySensor(data, names, units):
  for i in range(len(data)):
    print i, data[i]
    lcd.clear()
    lcd.message(names[i]+"\n")
    if (isinstance(data[i], basestring)): 
      lcd.message(data[i] + " " + units[i])
    else:
      lcd.message('{:0.3f}'.format(data[i]) + " " + units[i])
    sleep(2)
    
sensors = []
sensors.append(timesensor.TimeSensor())
sensors.append(si7021.SI7021Sensor())
sensors.append(tsl2561.TSL2561())
sensors.append(mpl3115a2.MPL3115A2())


if os.path.exists(logname):
  f = open(logname, 'a')
else:
  f = open(logname, 'w')
  names = []
  units = []
  for s in sensors:
    names = names + s.getNames()
    units = units + s.getUnits()
  f.write(','.join(names) + "\n")
  f.write(','.join(units) + "\n")
  
  

while(1):
  datapoint = []
  for s in sensors:
    data =  s.read()
    displaySensor(data, s.getNames(), s.getUnits())
    datapoint = datapoint + data
  f.write(','.join(str(x) for x in datapoint) + "\n")
    
    
  
    
