import pygame

from setings import*
from sprits import*
chasi = pygame.time.Clock()
import pygame.freetype
pygame.init()


window = pygame.display.set_mode((WIDTH,HEIGHT))
while play is True:
    last_events = pygame.event.get()
    for event in last_events:
        if event.type == pygame.QUIT:
            play = False
    
    
    window.fill((0, 0, 0))
    

    pygame.display.update()
    chasi.tick(15)
 