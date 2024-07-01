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
oled_i.fill(0)  # Clear the display

# Display dimensions
w = 120
h = 28

# Parameters for the spiral
t = 0  # Time parameter for animation
dt = 0.1  # Increment for the time parameter
r_max = 14  # Maximum radius of the spiral
r_min = 2   # Minimum radius of the spiral

# Main loop to animate the spiral
try:
    while True:
        oled_i.fill(0)  # Clear the screen
        t += dt  # Increment the time parameter
        for i in range(360):
            theta = math.radians(i)  # Convert angle to radians
            r = r_min + (r_max - r_min) * ((i % 360) / 360.0)  # Calculate radius
            x = int(r * math.cos(theta + t)) + w // 2  # Calculate x-coordinate
            y = int(r * math.sin(theta + t)) + h // 2  # Calculate y-coordinate
            if 0 <= x < w and 0 <= y < h:
                oled_i.pixel(x, y, 1) # Draw the pixel if it's within the display bounds
        oled_i.show()  # Update the display with the drawn pixels
        time.sleep_ms(5)  # Short delay to control the animation speed
except:
    oled_i.fill(0)
    oled_i.show()


