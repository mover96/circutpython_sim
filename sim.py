import pygame

num_pixels = 22
OFF = (0,0,0)

class Pixels:
    def __init__(self, num_pixels):
        self.pixels = [OFF] * num_pixels
        self.num_pixels = num_pixels
        self.screen = init_pygame()

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

def init_pygame():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("CircutPython Simulator")
     
    return  pygame.display.set_mode((1500,500))