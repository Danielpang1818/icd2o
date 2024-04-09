import sys
import pygame
 
pygame.init()
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
 
paddle_w = 20
paddle_h = 80
paddle1_x = 15
paddle1_y = SCREEN_HEIGHT // 2 - paddle_h // 2
paddle2_x = SCREEN_WIDTH - 15 - paddle_w
paddle2_y = SCREEN_HEIGHT // 2 - paddle_h // 2
player_speed = 7
 
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_radius = 15
ball_speed_x = 7
ball_speed_y = 7
 
score1 = 0
score2 = 0
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
 
clock = pygame.time.Clock()
 
running = True
while running:
    screen.fill(WHITE)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    pygame.draw.rect(screen, BLACK, [paddle1_x, paddle1_y, paddle_w, paddle_h])
    pygame.draw.rect(screen, BLACK, [paddle2_x, paddle2_y, paddle_w, paddle_h])
   
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
 
 
    score_text = FONT.render(f"{score1} - {score2}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))
 
    clock.tick(60)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= player_speed
        paddle1_y = max(paddle1_y, 0)  
    if keys[pygame.K_s]:
        paddle1_y += player_speed
        paddle1_y = min(paddle1_y, SCREEN_HEIGHT - paddle_h)  
    if keys[pygame.K_UP]:
        paddle2_y -= player_speed
        paddle2_y = max(paddle2_y, 0)  
    if keys[pygame.K_DOWN]:
        paddle2_y += player_speed
        paddle2_y = min(paddle2_y, SCREEN_HEIGHT - paddle_h)  
 
    ball_x += ball_speed_x
    ball_y += ball_speed_y
 
    if ball_y + ball_radius > SCREEN_HEIGHT or ball_y - ball_radius < 0:
        ball_speed_y *= -1
 
    if paddle1_x <= ball_x <= paddle1_x + paddle_w and paddle1_y <= ball_y <= paddle1_y + paddle_h:
        ball_speed_x *= -1
    elif paddle2_x <= ball_x <= paddle2_x + paddle_w and paddle2_y <= ball_y <= paddle2_y + paddle_h:
        ball_speed_x *= -1
 
    if ball_x + ball_radius < 0:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_speed_x *= -1
        score2 += 1
    elif ball_x - ball_radius > SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_speed_x *= -1
        score1 += 1
 
    pygame.display.flip()
 
pygame.quit()
sys.exit()
