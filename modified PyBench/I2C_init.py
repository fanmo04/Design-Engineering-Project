import pyb
import math
from pyb import LED, ADC, Pin, I2C
from oled_938 import OLED_938
from bme280 import BME280

b_LED = LED(4)
pot = ADC(Pin('X11'))

oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64, external_vcc=False, i2c_devid=61)
oled.poweron()
oled.init_display()

oled.draw_text(0,0,'Hello World!')
oled.display()

pressure = I2C(1, I2C.MASTER)
pressure.init(I2C.MASTER, baudrate=9600)
#presuure.init(I2C.SLAVE, addr=0x77)
print (pressure)
BMP280 = BME280(1,0x76,pressure)

oled.draw_text(0,9,'done')
oled.display()

