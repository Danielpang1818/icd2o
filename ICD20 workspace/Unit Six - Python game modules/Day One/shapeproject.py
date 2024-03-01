import sys
import math
import pygame


pygame.init()

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLUE = (204,255,255)
DARK_BLUE = (0,0,255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)
LIGHT_RED = (255,51,51)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Pygame Project")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((WHITE))

    pygame.draw.rect(screen,BLUE, (35,0,180,400))
    pygame.draw.rect(screen,BLUE, (0,35,250,330))
    pygame.draw.circle(screen, BLUE, (35, 35),35)
    pygame.draw.circle(screen, BLUE, (35, 365),35)
    pygame.draw.circle(screen, BLUE, (215, 365),35)
    pygame.draw.circle(screen, BLUE, (215, 35),35)

    pygame.draw.line(screen, RED, (0,31),(250,31),4)
    pygame.draw.line(screen, RED, (0,361),(250,361),4)
    pygame.draw.line(screen, RED, (0,205),(250,205),5)

    pygame.draw.circle(screen, RED, (50, 75),3)
    pygame.draw.circle(screen, RED, (200, 75),3)
    pygame.draw.circle(screen, RED, (50, 160),3)
    pygame.draw.circle(screen, RED, (200, 160),3)
    pygame.draw.circle(screen, RED, (50, 240),3)
    pygame.draw.circle(screen, RED, (200, 240),3)
    pygame.draw.circle(screen, RED, (50, 325),3)
    pygame.draw.circle(screen, RED, (200, 325),3)

    pygame.draw.line(screen, DARK_BLUE, (0,140),(250,140),7)
    pygame.draw.line(screen, DARK_BLUE, (0,260),(250,260),7)

    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(30, 55, 40, 40),0,math.pi*2,2)
    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(180, 55, 40, 40),0,math.pi*2,2)
    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(30, 305, 40, 40),0,math.pi*2,2)
    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(180, 305, 40, 40),0,math.pi*2,2)

    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(105, 185, 40, 40),0,math.pi*2,2)
    pygame.draw.circle(screen, RED, (125, 205),5)

    pygame.draw.arc(screen, LIGHT_RED, pygame.Rect(105, 340, 40, 40),0,math.pi,2)
    pygame.draw.arc(screen, LIGHT_RED, (105, 15, 40, 40), math.pi, 2 * math.pi, 2)

    pygame.draw.aalines(screen, BLACK, True, [(-3,190),(20,190),(20,220),(-3,220)])
    

    pygame.display.flip()

pygame.quit()