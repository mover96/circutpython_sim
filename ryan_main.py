import time
from sim import Pixels

num_pixels = 22

pixels = Pixels(num_pixels)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
PINK = (255, 0, 127)
OFF = (0, 0, 0)

color_list = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def explode(wait, times):
    for _ in range (times):  
        for j in range (len(color_list)):
            color = color_list[j]
            for i in range (int(num_pixels / 2)):
                pixels[11 + i] = color
                pixels[10 - i] = color
                pixels.show()
                time.sleep(wait)

def init_tape():
    tape = []
    for color in color_list:
        for _ in range (4):
            tape.append(color)
        for _ in range (3):
            tape.append(OFF)
    return tape

def write_tape(tape):
    for pixel in range (num_pixels):
        pixels[pixel] = tape[pixel]
    pixels.show()

def update_tape(tape):
    return tape[1:] + tape[:1]

def blaster(tape, times, wait):
    for _ in range (times * 49):
        write_tape(tape)
        tape = update_tape(tape)
        time.sleep(wait)

def swipe(wait, times):
    x = 1
    for _ in range (times):
            for j in range (len(color_list)):
                color = color_list[j]
                if (x == 1):
                    for i in range (num_pixels): 
                        pixels[i] = color
                        pixels.show()
                        time.sleep(wait)
                    x = 0
                else:
                    for i in range (num_pixels - 1, -1, -1): 
                        pixels[i] = color
                        pixels.show()
                        time.sleep(wait)
                    x = 1

tape = init_tape()
while True:
    
    swipe(.05, 1)
    explode(.05, 4)
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(.5)
    pixels.fill(PURPLE)
    pixels.show()
    time.sleep(.5)
    pixels.fill(PINK)
    pixels.show()
    time.sleep(.5)
    blaster(tape, 4, .05)

    # color_chase(RED, 0.1)
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)

    # rainbow_cycle(0)
