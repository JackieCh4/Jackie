# Circuit Playground NeoPixel
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0 , 0)

while True:

    if switch.value:
        pixels.fill(RED)
        pixels.show()
    else:
        pixels.fill(BLANK)
        pixels.show()

    time.sleep(0.1)


