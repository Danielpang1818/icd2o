import sys

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket Drawing")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)

while True:
    screen.fill(WHITE)

    pygame.draw.rect(screen,RED, (400,100,150,500))
    pygame.draw.polygon(screen,YELLOW,[(475,25),(400,100),(550,100)])
    pygame.draw.rect(screen,BLACK, (350,200,50,380))
    pygame.draw.rect(screen,BLACK, (550,200,50,380))
    pygame.draw.line(screen,WHITE,(450,100),(400,600),5)
    pygame.draw.line(screen,WHITE,(460,100),(410,600),5)
    pygame.draw.line(screen,WHITE,(470,100),(420,600),5)

    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()