import sys

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Drawing")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)

while True:
    screen.fill(WHITE)

    pygame.draw.rect(screen, YELLOW, (350, 300, 300, 100))
    pygame.draw.rect(screen, BLUE, (400, 320, 80, 45))
    pygame.draw.rect(screen, BLUE, (500, 320, 80, 45))

    pygame.draw.circle(screen, BLACK, (400, 400), 20)
    pygame.draw.circle(screen, BLACK, (600, 400), 20)

    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()