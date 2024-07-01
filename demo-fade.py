import time
import ws2812b
import machine

# Initialize Button
buttonport = 12
button = machine.Pin(buttonport, machine.Pin.IN, machine.Pin.PULL_UP)

# Initialize RGB LEDs with 2 pixels
numpix = 2
strip = ws2812b.ws2812b(numpix, 0, 22)

# Define maximum brightness value for channels
MAX = 60

# Define RGB color tuples
OFF = (0, 0 ,0) 
RED = (MAX, 0, 0)
ORANGE = (MAX, MAX-30, 0)
YELLOW = (MAX, MAX-5, 0)
GREEN = (0, MAX, 0)
BLUE = (0, 0, MAX)
INDIGO = (MAX//4, 0, MAX//2)
VIOLET = (MAX//2, MAX//5, MAX-40)
WHITE = (MAX, MAX, MAX)

# List of colors for transitions
colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, WHITE]

# Smoothly transitions LED 0 from one color to the next
def fade_to_color(start_color, end_color, step_r, step_g, step_b, maxsteps, step):
    new_r = int(start_color[0] + step_r * step)
    new_g = int(start_color[1] + step_g * step)
    new_b = int(start_color[2] + step_b * step)
    strip.set_pixel(0, new_r, new_g, new_b)

# Calculates steps between colors for smooth transition
def calc_next(cidx, maxsteps, colors):
    c1 = colors[(cidx+len(colors)-1)%len(colors)]
    c2 = colors[cidx]
    step_r = (c2[0] - c1[0]) / maxsteps
    step_g = (c2[1] - c1[1]) / maxsteps
    step_b = (c2[2] - c1[2]) / maxsteps
    return c1, c2, step_r, step_g, step_b

# Initialize both LEDs to 'off' state
strip.fill(OFF[0], OFF[1], OFF[2])
strip.show()

# Initial setup for transition cycle
step = 0
maxsteps = 20
cidx = 0
isactive = True

try:
    while True:
        
        if button.value() == 0:
            isactive = not isactive
            while button.value() == 0:
                pass
        
        if isactive:
            # Check and prepare for next color transition
            if step == 0:
                cidx = (cidx + 1) % len(colors)
                c1, c2, step_r, step_g, step_b = calc_next(cidx, maxsteps, colors)
                # Set the second LED the target color
                strip.set_pixel(1, c2[0], c2[1], c2[2])
                
            # Execute non-blocking fade between colors
            fade_to_color(c1, c2,  step_r, step_g, step_b, maxsteps, step)
            
            # Increment step within the transition phase
            step = (step + 1) % maxsteps
                
            # Refresh LED display to update colors
            strip.show()
        
        # Delay briefly to pace the transition
        time.sleep(0.05)
        
except KeyboardInterrupt:
    # Turn off LEDs when script is interrupted
    strip.fill(OFF[0], OFF[1], OFF[2])
    strip.show()

