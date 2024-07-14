from machine import Pin, I2C
from ssd1312 import SSD1312_I2C
import framebuf, sys
import time
import math

# Initialize the display
Pin(8, Pin.IN, Pin.PULL_UP)
Pin(9, Pin.IN, Pin.PULL_UP)
RST = 11
rst = Pin(RST, Pin.OUT)
rst(1)
time.sleep_ms(100)
rst(0)
time.sleep_ms(100)
rst(1)
time.sleep_ms(100)
i2c_dev0 = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled_i = SSD1312_I2C(120, 28, i2c_dev0)
oled_i.fill(0) # Clear the display
oled_i.rotate(1) # optional: rotate the display by 180deg

#display dimensions
w = 120
h = 28

# set a single pixel
# oled_i.pixel(16, 5, 1)
# oled_i.show()

# define some shapes
def hline(x1, x2, y):
    for x in range(x1, x2, 1):
        oled_i.pixel(x, y, 1)

def vline(y1, y2, x):
    for y in range(y1, y2, 1):
        oled_i.pixel(x, y, 1)

def rect(border):
    hline(border, w-border, border)
    hline(border, w-border, h-border)
    vline(border, h-border, border)
    vline(border, h-border, w-border)

def spiral():
    r_max = 12
    r_min = 2
    for i in range(360):
        theta = math.radians(i)
        r = r_min + (r_max - r_min) * ((i % 360) / 360.0)
        x = int(r * math.cos(theta)) + w // 2
        y = int(r * math.sin(theta)) + h // 2
        if 0 < x < w and 0 <= y < h:
            oled_i.pixel(x, y, 1)

def sinewave():
    amplitude = h // 4
    frequency = 2
    for x in range(w):
        y = int((h // 2) + amplitude * math.sin(2 * math.pi * frequency * (x / w)))
        if 0 <= y < h:
            oled_i.pixel(x, y, 1)

def sinewave_ani():
    base_amplitude = h // 4
    frequency = 2
    for phase in range(360):
        oled_i.fill(0)
        amplitude = base_amplitude - int((base_amplitude / 2) * math.sin(math.radians(phase * 8)))
        for x in range(w):
            y = int((h / 2) + amplitude * math.sin(2 * math.pi * frequency * (x / w) + math.radians(phase * 8)))
            if 0 <= y < h:
                oled_i.pixel(x, y, 1)
        oled_i.show()
        time.sleep_ms(1)

# # render rect
# rect(5)
# oled_i.show()

# # render spiral
# spiral()
# oled_i.show()

# # render sine wave
# sinewave()
# oled_i.show()

# sine wave animation
sinewave_ani()
