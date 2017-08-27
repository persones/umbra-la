# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# SI7021
# This code is designed to work with the SI7021_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Humidity?sku=SI7021_I2CS#tabs-0-product_tabset-2

import smbus
import time

class SI7021Sensor:
  def __init__(self):
    self.bus = smbus.SMBus(1)
    
  def read(self):
    # Get I2C bus
    

    # SI7021 address, 0x40(64)
    #		0xF5(245)	Select Relative Humidity NO HOLD master mode
    self.bus.write_byte(0x40, 0xF5)

    time.sleep(0.3)

    result = []

    # SI7021 address, 0x40(64)
    # Read data back, 2 bytes, Humidity MSB first
    data0 = self.bus.read_byte(0x40)
    data1 = self.bus.read_byte(0x40)

    # Convert the data
    result.append(((data0 * 256 + data1) * 125 / 65536.0) - 6)

    time.sleep(0.3)

    # SI7021 address, 0x40(64)
    #		0xF3(243)	Select temperature NO HOLD master mode
    self.bus.write_byte(0x40, 0xF3)

    time.sleep(0.3)

    # SI7021 address, 0x40(64)
    # Read data back, 2 bytes, Temperature MSB first
    data0 = self.bus.read_byte(0x40)
    data1 = self.bus.read_byte(0x40)

    # Convert the data
    ctemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    result.append(ctemp)
    result.append(ctemp * 1.8 + 32)

    for i in range (len(result)):
      result[i] = round(result[i],3)
    return result

  def getNames(self):
    return ["humidity", "si_temp_c", "si_temp_f"]
  
  def getUnits(self):
    return ["%", "deg C", "deg F"]
    # Output data to screen
    #print "Relative Humidity is : %.2f %%" %humidity
    #print "Temperature in Celsius is : %.2f C" %cTemp
    #print "Temperature in Fahrenheit is : %.2f F" %fTemp
