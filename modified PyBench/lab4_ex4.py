import pyb
import math
from pyb import LED, ADC, Pin
from oled_938 import OLED_938

b_LED = LED(4)
pot = ADC(Pin('X11'))

oled = OLED_938(pinout={'sda': 'Y10', 'scl': 'Y9', 'res': 'Y8'}, height=64, external_vcc=False, i2c_devid=61)
oled.poweron()
oled.init_display()

#oled.draw_text(28,0,'Hello World!')

tic=pyb.millis()
while True:
    b_LED.toggle()
    toc=pyb.millis()
    #oled.draw_text(0,20,'Delay time: {:6.f}sec'.format((toc-tic)*0.001))
    #oled.draw_text(0,40, 'POT5K reading:{:5d}'.format(pot.read()))

    value = (math.pi * pot.read()/4095.0)
    #oled.draw_text(0, 20, 'Value:{:3.2f}'.format(value))

    xvalue = int(60*(-1 * math.cos(value) + 1))
    yvalue = int(60* math.sin(value))

    oled.draw_circle(xvalue, yvalue, 4, 1)
    oled.draw_line(58, 0, xvalue, yvalue, 1)

    tic=pyb.millis()
    oled.display()
    oled.draw_circle(xvalue, yvalue, 4, 0)
    oled.draw_line(58, 0, xvalue, yvalue, 0)