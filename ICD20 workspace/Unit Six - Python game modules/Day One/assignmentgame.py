import sys
import pygame
import math
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Application")

car_color = (0, 0, 255)
car_x = SCREEN_WIDTH // 2
car_y = SCREEN_HEIGHT // 2
car_size = 30
car_speed = 5
x_vel = 0
y_vel = 0
RED = (255,0,0)
laps_completed = 0


font = pygame.font.SysFont(None, 18)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill((255, 255, 255))


    #racetrack
    racetrack = [
        pygame.Rect(0, 0, SCREEN_WIDTH, 10), #boundary 
        pygame.Rect(0, SCREEN_HEIGHT-10, SCREEN_WIDTH, 10), #boundary 
        pygame.Rect(125, 150, 650, 10),
        pygame.Rect(250, 300, 400, 10),
        pygame.Rect(400, 460, 250, 10),
    
        pygame.Rect(0, 0, 10, SCREEN_HEIGHT), #boundary 
        pygame.Rect(SCREEN_WIDTH-10,0, 10, SCREEN_HEIGHT), #boundary 
        pygame.Rect(125, 150, 10, 375),
        pygame.Rect(775, 150, 10, 300),
        pygame.Rect(250, 300, 10, 350),
    ]

    #finish line
    finishline = [
        pygame.Rect(150,150,75,10)
    ]

    for rect in finishline:
        pygame.draw.rect(screen, (35,0,0), rect)

    for rect in racetrack:
        pygame.draw.rect(screen, (255, 0, 0), rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x_vel > -7 :
        #car_x -= car_speed
        #car_x = max(car_x, 0)
        x_vel -= 0.1
    if keys[pygame.K_d] and x_vel < 7:
        # car_x += car_speed
        #car_x = min(car_x, SCREEN_WIDTH - car_size)
        x_vel += 0.1

    if keys[pygame.K_w] and y_vel > - 7:
        # car_y -= car_speed
        #car_y = max(car_y, 0)
        y_vel -= 0.1
    if keys[pygame.K_s] and y_vel < 7:
        # car_y += car_speed
        #car_y = min(car_y, SCREEN_HEIGHT - car_size)
        y_vel += 0.1
    car_x += x_vel
    car_y += y_vel

    car_rect = pygame.Rect(car_x, car_y, car_size, car_size)
    for rect in racetrack:
        if car_rect.colliderect(rect):
            
            x_vel = 0
            y_vel = 0
            break 

    for rect in finishline:
        if car_rect.colliderect(rect):
            x_vel = 0
            y_vel = 0
            laps_completed += 1  #laps completed
            break

    car_y = max(car_y, 0)
    car_y = min(car_y, SCREEN_HEIGHT - car_size)
    car_x = min(car_x, SCREEN_WIDTH - car_size)
    car_x = max(car_x, 0)
    pygame.draw.rect(screen, car_color, (car_x, car_y, car_size, car_size))

    laps_text = font.render(f"Laps: {laps_completed}", True, (0, 0, 0))
    screen.blit(laps_text, (20, 20))

    pygame.display.flip()

pygame.quit()
