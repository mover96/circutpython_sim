import time

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

color_list = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]

def init_tape():
    tape = []
    for color in color_list:
        for _ in range (4):
            tape.append(color)
        for _ in range (4):
            tape.append(OFF)
    return tape

def write_tape(pixels, tape):
    for i in range(len(pixels)):
        pixels[i] = tape[i]
    pixels.show()

def update_tape(tape):
    return tape[1:] + tape[:1]

def blaster(pixels, tape, times):
    for _ in range (times * 48):
        write_tape(pixels, tape)
        tape = update_tape(tape)
        time.sleep(.1)

tape = init_tape()
def the_loop(pixels):
    blaster(pixels, tape, 2)
