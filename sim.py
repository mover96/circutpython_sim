# import the pygame module, so you can use it
import pygame
import time
from myloop import the_loop

num_pixels = 22
OFF = (0,0,0)

class Pixels:
    def __init__(self, screen, num_pixels):
        self.pixels = [OFF] * num_pixels
        self.num_pixels = num_pixels
        self.screen = screen

    def show(self):
        self.screen.fill(OFF)
        for count, pixel in enumerate(self.pixels):
            x_offset = count * 55
            border = pygame.Rect((48 + x_offset, 148), (44,44))
            rect = pygame.Rect((50 + x_offset, 150), (40, 40))
            pygame.display.update(pygame.draw.rect(self.screen, (255,255,255), border))
            pygame.display.update(pygame.draw.rect(self.screen, pixel, rect))
    
    def __getitem__(self, index):
        return self.pixels[index]
    
    def __setitem__(self, index, value):
        self.pixels[index] = value
    
    def __len__(self):
        return len(self.pixels)

    def count(self):
        return len(self.pixels)

 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("CircutPython Simulator")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1500,500))
     
    # define a variable to control the main loop
    running = True

    pixels = Pixels(screen, num_pixels)
     
    # main loop
    while running:
        the_loop(pixels)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()