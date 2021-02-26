# Circuit Playground NeoPixel
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT

button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.DOWN

button_B = DigitalInOut(board.D4)
button_B.direction = Direction.INPUT
button_B.pull = Pull.DOWN

button_APre = False
button_BPre = False

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0 , 0)
ORANGE = (255, 165, 0)

while True:

    if switch.value:
        if button_A.value != button_APre:
            button_APre = button_A.value

            if not button_APre:
                color = ORANGE
        elif button_B.value != button_BPre:
            button_BPre = button_B.value

            if not button_BPre:
                color = BLUE
        pixels.fill(color)

    else:
        color = RED
        pixels.fill(BLANK)

    time.sleep(0.01)



