import pyb
from pyb import LED, ADC, Pin
from oled_938 import OLED_938
from mpu6050 import *

b_LED = LED(4)
pot = ADC(Pin('X11'))

oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64, external_vcc=False, i2c_devid=61)
oled.poweron()
oled.init_display()

imu = MPU6050(1, False)

tic=pyb.millis()
while True:
    b_LED.toggle()
    toc = pyb.millis()

    oled.draw_text(0,20, 'Pitch Angle:{:3.2f}'.format(imu.pitch()))
    oled.draw_text(0,40, 'Rate of Pitch:{:3.2f}'.format(imu.get_gy()))

    tic = pyb.millis()
    oled.display()
    delay = pyb.rng() % 1000
    pyb.delay(delay)