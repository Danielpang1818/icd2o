import sys
import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Pygame Application")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# fill
    screen.fill((255,255,255))
    pygame.display.flip()

pygame.quit()