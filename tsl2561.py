import smbus
import time

# Get I2C bus

class TSL2561:
  def __init__(self):
    self.bus = smbus.SMBus(1)
    
  def read(self):
    result = []
    # TSL2561 address, 0x39(57)
    # Select control register, 0x00(00) with command register, 0x80(128)
    #		0x03(03)	Power ON mode
    self.bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
    # TSL2561 address, 0x39(57)
    # Select timing register, 0x01(01) with command register, 0x80(128)
    #		0x02(02)	Nominal integration time = 402ms
    self.bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

    time.sleep(0.5)

    # Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
    # ch0 LSB, ch0 MSB
    data = self.bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

    # Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
    # ch1 LSB, ch1 MSB
    data1 = self.bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

    # Convert the data
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]

    result.append(ch0)
    result.append(ch1)
    result.append(ch0 - ch1)
    
    return result

  def getNames(self):
    return ["full_spectrum", "infrared", "visible"]
  
  def getUnits(self):
    return ["lux", "lux", "lux"]
    
  # Output data to screen
#print "Full Spectrum(IR + Visible) :%d lux" %ch0
#print "Infrared Value :%d lux" %ch1
#print "Visible Value :%d lux" %(ch0 - ch1)