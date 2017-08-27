
import time
import datetime

class TimeSensor:
  def __init__(self):
    pass
    
  def read(self):
    return [datetime.datetime.utcnow().isoformat()]

  def getNames(self):
    return ["time"]
  
  def getUnits(self):
    return ["UTC"]
    # Output data to screen
    #print "Relative Humidity is : %.2f %%" %humidity
    #print "Temperature in Celsius is : %.2f C" %cTemp
    #print "Temperature in Fahrenheit is : %.2f F" %fTemp
