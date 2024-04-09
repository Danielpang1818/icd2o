import pygame
import time
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Application")

player1_color = (0, 0, 255)
player2_color = (0, 255, 0)

player1_x = 250
player1_y = 100
player2_x = 200
player2_y = 75

car_size = 30
car_speed = 5

player1_x_vel = 0
player1_y_vel = 0
player2_x_vel = 0
player2_y_vel = 0

laps_completed = 0
finish_line_x = 500
finish_line_y = 0
finish_line_width = 10
finish_line_height = 160

player1_laps = 0
player2_laps = 0
laps_to_win = 3

checkpoint_x = 400
checkpoint_y = 0
checkpoint_width = 10
checkpoint_height = 160


running = True
finish_line_visible = True
winner = None

firstfont = pygame.font.SysFont(None, 20)
secondfont = pygame.font.SysFont(None,50)


background_image = pygame.image.load('spacebackground.jpg').convert()

background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


player1_image = pygame.image.load('spaceship.png').convert_alpha()
player2_image = pygame.image.load('ufo2.jpg').convert_alpha()
player1_image = pygame.transform.scale(player1_image, (car_size, car_size))
player2_image = pygame.transform.scale(player2_image, (car_size, car_size))

collision_sound = pygame.mixer.Sound('collision.wav')
checkpoint_sound = pygame.mixer.Sound('checkpoint.wav')

pygame.mixer.music.load('backgroundmusic.wav')
pygame.mixer.music.play(-1) 

for i in range(3, 0, -1):
    screen.blit(background_image, (0, 0))
    countdown_text = secondfont.render(str(i), True, (255, 255, 255))
    screen.blit(countdown_text, (SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 25))
    pygame.display.flip()
    time.sleep(1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.blit(background_image, (0, 0))

    # Racetrack boundaries
    racetrack = [
        pygame.Rect(0, 0, SCREEN_WIDTH, 10),  # Top boundary
        pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),  # Bottom boundary
        pygame.Rect(125, 150, 650, 10),
        pygame.Rect(250, 300, 400, 10),
        pygame.Rect(400, 450, 385, 10),
        pygame.Rect(0, 0, 10, SCREEN_HEIGHT),  # Left boundary
        pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT),  # Right boundary
        pygame.Rect(125, 150, 10, 375),
        pygame.Rect(775, 150, 10, 300),
        pygame.Rect(250, 300, 10, 350),
    ]

    # Draw racetrack boundaries
    for rect in racetrack:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    # Finish line
    if finish_line_visible:
        finish_line_rect = pygame.Rect(finish_line_x, finish_line_y, finish_line_width, finish_line_height)
        pygame.draw.rect(screen, (0, 0, 0), finish_line_rect)


    checkpoint_rect = pygame.Rect(checkpoint_x, checkpoint_y, checkpoint_width, checkpoint_height)
    pygame.draw.rect(screen, (255, 255, 255), checkpoint_rect)

    # Player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1_x_vel > -7: # normal acceleration
        player1_x_vel -= 0.1
    if keys[pygame.K_a] and player1_x_vel > -7 and player1_x_vel > 4: #Slows down faster at high speeds
        player1_x_vel -= 0.2
    if keys[pygame.K_d] and player1_x_vel < 7:
        player1_x_vel += 0.1
    if keys[pygame.K_d] and player1_x_vel < 7 and player1_x_vel < -4:
        player1_x_vel += 0.2
    if keys[pygame.K_w] and player1_y_vel > -7:
        player1_y_vel -= 0.1
    if keys[pygame.K_w] and player1_y_vel > -7 and player1_y_vel > 4:
        player1_y_vel -= 0.2
    if keys[pygame.K_s] and player1_y_vel < 7:
        player1_y_vel += 0.1
    if keys[pygame.K_s] and player1_y_vel < 7 and player1_y_vel < -4:
        player1_y_vel += 0.2
        #player 2
    if keys[pygame.K_LEFT] and player2_x_vel > -7: # normal acceleration
        player2_x_vel -= 0.1
    if keys[pygame.K_LEFT] and player2_x_vel > -7 and player2_x_vel > 4: #Slows down faster at high speeds
        player2_x_vel -= 0.2
    if keys[pygame.K_RIGHT] and player2_x_vel < 7:
        player2_x_vel += 0.1
    if keys[pygame.K_RIGHT] and player2_x_vel < 7 and player2_x_vel < -4:
        player2_x_vel += 0.2
    if keys[pygame.K_UP] and player2_y_vel > -7:
        player2_y_vel -= 0.1
    if keys[pygame.K_UP] and player2_y_vel > -7 and player2_y_vel > 4:
        player2_y_vel -= 0.2
    if keys[pygame.K_DOWN] and player2_y_vel < 7:
        player2_y_vel += 0.1
    if keys[pygame.K_DOWN] and player2_y_vel < 7 and player2_y_vel < -4:
        player2_y_vel += 0.2

    # Update car position
    player1_x += player1_x_vel
    player1_y += player1_y_vel
    player2_x += player2_x_vel
    player2_y += player2_y_vel


    

    # boundaries
    car_rect = pygame.Rect(player1_x, player1_y, car_size, car_size)
    for rect in racetrack:
        if car_rect.colliderect(rect):
            player1_x_vel = 0
            player1_y_vel = 0
            collision_sound.play()
            break

            #player 2
    car_rect = pygame.Rect(player2_x, player2_y, car_size, car_size)
    for rect in racetrack:
        if car_rect.colliderect(rect):
            player2_x_vel = 0
            player2_y_vel = 0
            collision_sound.play()
            break

    player1_rect = pygame.Rect(player1_x, player1_y, car_size, car_size)
    player2_rect = pygame.Rect(player2_x, player2_y, car_size, car_size)

    


    if finish_line_visible and player1_rect.colliderect(finish_line_rect) and winner is None:
        finish_line_visible = False
        player1_laps += 1
        checkpoint_sound.play()
        if player1_laps >= laps_to_win:
            winner = "Player 1"

    if finish_line_visible and player2_rect.colliderect(finish_line_rect) and winner is None:
        finish_line_visible = False
        player2_laps += 1
        checkpoint_sound.play()
        if player2_laps >= laps_to_win:
            winner = "Player 2"

    #checkpoint collide
    if player1_rect.colliderect(checkpoint_rect):
        finish_line_visible = True
    if player2_rect.colliderect(checkpoint_rect):
        finish_line_visible = True
        
    
    # boundaries
    player1_y = max(player1_y, 0)
    player1_y = min(player1_y, SCREEN_HEIGHT - car_size)
    player1_x = min(player1_x, SCREEN_WIDTH - car_size)
    player1_x = max(player1_x, 0)


    #player 2
    player2_y = max(player2_y, 0)
    player2_y = min(player2_y, SCREEN_HEIGHT - car_size)
    player2_x = min(player2_x, SCREEN_WIDTH - car_size)
    player2_x = max(player2_x, 0)

    # Draw car
    screen.blit(player1_image, (player1_x, player1_y))
    screen.blit(player2_image, (player2_x, player2_y))


    lap_count_text = firstfont.render(f"Player 1 Laps: {player1_laps}/{laps_to_win}   Player 2 Laps: {player2_laps}/{laps_to_win}", True, (255, 255, 255))
    screen.blit(lap_count_text, (10, 10))

    if winner:
        winner_text = secondfont.render(f"{winner} Wins!", True, (255, 0, 0))
        screen.blit(winner_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
