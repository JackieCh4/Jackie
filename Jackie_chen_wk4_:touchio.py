import time
import board
import touchio
import neopixel

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)
r = g = b = 0
color = (r, g, b)
blank = (0, 0, 0)


while True:

    if touch_A1.value:
        r += 3
        if r > 255:
            r = 255
        print(r)
        pixels.fill((r, g, b))

    if touch_A2.value:
        r -= 3
        if r < 0:
            r = 0
        pixels.fill((r, g, b))

    if touch_A3.value:
        g += 3
        if g > 255:
            g = 255
        pixels.fill((r, g, b))

    if touch_A4.value:
        g -= 3
        if g < 0:
            g = 0
        pixels.fill((r, g, b))

    if touch_A5.value:
        b += 3
        if b > 255:
            b = 255
        pixels.fill((r, g, b))

    if touch_A6.value:
        b -= 3
        if b < 0:
            b = 0
        pixels.fill((r, g, b))

    if touch_TX.value:
        pixels.fill(blank)

    time.sleep(0.01)
