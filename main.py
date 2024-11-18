import pygame
from display import Display
SCREENSIZE = [1000, 800]
screen = pygame.display.set_mode((1000, 800))

pygame.init()
pygame.font.init() 
zoom = 1
my_font = pygame.font.SysFont('Comic Sans MS', 30)
displays = Display()
running = True


def welcomescreen():
    welcomesc = True
    
    
    while welcomesc:
        
        
        
        
        displays.disp()


while running:
    welcomescreen()
    
    
    



