import sys

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sun drawing")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen,YELLOW,(450,300),50)
    pygame.draw.lines(screen,YELLOW,False,[(360,300),(450,300),(375,275),(450,300),(400,250),(450,300),(425,200),(450,300),(450,100),(450,300)(475,275),(450,300),(475,200),],10)

    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()