import pygame

num_pixels = 22
OFF = (0,0,0)
border_color = (255,255,255)

window_width = 500
border_x = 48
border_y = 148
border_len = 44
pixel_x = 50
pixel_y = 150
pixel_side = 40

class Pixels:
    def __init__(self, num_pixels):
        self.pixels = [OFF] * num_pixels
        self.num_pixels = num_pixels
        self.screen = init_pygame()

    def show(self):
        self.screen.fill(OFF)
        for count, pixel in enumerate(self.pixels):
            x_offset = count * 55
            border = pygame.Rect((border_x + x_offset, border_y), (border_len, border_len))
            rect = pygame.Rect((pixel_x + x_offset, pixel_y), (pixel_side, pixel_side))
            pygame.display.update(pygame.draw.rect(self.screen, border_color, border))
            pygame.display.update(pygame.draw.rect(self.screen, pixel, rect))
    
    def __getitem__(self, index):
        return self.pixels[index]
    
    def __setitem__(self, index, value):
        self.pixels[index] = value
    
    def __len__(self):
        return len(self.pixels)

    def count(self):
        return len(self.pixels)
    
    def fill(self, color):
        for i in range(len(self.pixels)):
            self.pixels[i] = color

def init_pygame():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("CircutPython Simulator")
     
    return  pygame.display.set_mode((1500, window_width))