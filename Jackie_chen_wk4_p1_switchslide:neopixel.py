import time
import board
import neopixel
import analogio
from simpleio import map_range

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.15)

brightchange = analogio.AnalogIn(board.A1)
colorchange = analogio.AnalogIn(board.A2)

smooth_val = brightchange.value

def Smooth(x, y, z):
    x = z * y + ((1 - z) * x)
    return x

color = (0, 0, 255)
pixels.fill(color)
bright = 0

while True:

    bc = brightchange.value
    smooth_val = Smooth(smooth_val, bc, 0.25)

    scaled_val = map_range(smooth_val, 0, 65535, 0, 1)
    scaled_val = float(scaled_val)
    bright = scaled_val

    color = (int(bright * 0), int(bright * 0), int(bright * 255))
    pixels.fill(color)

    cc = colorchange.value
    print((bright,))

    if cc > 60000:
        color = (int(255 * bright), 0, int(100 * bright))
        pixels.fill(color)

    else:
        color = (int(100 * bright), 0, int(255 * bright))
        pixels.fill(color)

    time.sleep(0.01)
