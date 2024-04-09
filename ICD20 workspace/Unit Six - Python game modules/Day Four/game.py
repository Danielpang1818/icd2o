import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Application")

player1_color = (0, 0, 255)
player2_color = (0, 255, 0)

player1_x = 200
player1_y = 100
player2_x = 300
player2_y = 100

car_size = 30
car_speed = 5

player1_x_vel = 0
player1_y_vel = 0
player2_x_vel = 0
player2_y_vel = 0

laps_completed_player1 = 0
laps_completed_player2 = 0

finish_line_x = 200
finish_line_y = 0
finish_line_width = 10
finish_line_height = 160

font = pygame.font.SysFont(None, 18)

player1_passed_finish_line = False
player2_passed_finish_line = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill((255, 255, 255))

    # Racetrack boundaries
    racetrack = [
        pygame.Rect(0, 0, SCREEN_WIDTH, 10),  # Top boundary
        pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),  # Bottom boundary
        pygame.Rect(125, 150, 650, 10),
        pygame.Rect(250, 300, 400, 10),
        pygame.Rect(400, 460, 250, 10),
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
    finish_line_rect = pygame.Rect(finish_line_x, finish_line_y, finish_line_width, finish_line_height)
    pygame.draw.rect(screen, (0, 0, 0), finish_line_rect)

    # Player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_x_vel -= 0.1
    if keys[pygame.K_d]:
        player1_x_vel += 0.1
    if keys[pygame.K_w]:
        player1_y_vel -= 0.1
    if keys[pygame.K_s]:
        player1_y_vel += 0.1

    # Player 2
    if keys[pygame.K_LEFT]:
        player2_x_vel -= 0.1
    if keys[pygame.K_RIGHT]:
        player2_x_vel += 0.1
    if keys[pygame.K_UP]:
        player2_y_vel -= 0.1
    if keys[pygame.K_DOWN]:
        player2_y_vel += 0.1

    # Update player positions
    player1_x += player1_x_vel
    player1_y += player1_y_vel
    player2_x += player2_x_vel
    player2_y += player2_y_vel

    # Check collisions with racetrack boundaries for Player 1
    player1_rect = pygame.Rect(player1_x, player1_y, car_size, car_size)
    for rect in racetrack:
        if player1_rect.colliderect(rect):
            player1_x_vel = 0
            player1_y_vel = 0
            break

    # Check collisions with racetrack boundaries for Player 2
    player2_rect = pygame.Rect(player2_x, player2_y, car_size, car_size)
    for rect in racetrack:
        if player2_rect.colliderect(rect):
            player2_x_vel = 0
            player2_y_vel = 0
            break

    # Check if Player 1 passes the finish line
    if player1_rect.right > finish_line_x + finish_line_width and not player1_passed_finish_line:
        player1_passed_finish_line = True
    elif player1_rect.left < finish_line_x + finish_line_width:
        if player1_passed_finish_line:
            laps_completed_player1 += 1
            player1_passed_finish_line = False

    # Check if Player 2 passes the finish line
    if player2_rect.right > finish_line_x + finish_line_width and not player2_passed_finish_line:
        player2_passed_finish_line = True
    elif player2_rect.left < finish_line_x + finish_line_width:
        if player2_passed_finish_line:
            laps_completed_player2 += 1
            player2_passed_finish_line = False

    # Draw Player 1
    pygame.draw.rect(screen, player1_color, (player1_x, player1_y, car_size, car_size))

    # Draw Player 2
    pygame.draw.rect(screen, player2_color, (player2_x, player2_y, car_size, car_size))

    # Display laps completed for each player
    laps_text_player1 = font.render(f"Player 1 Laps: {laps_completed_player1}", True, (0, 0, 0))
    laps_text_player2 = font.render(f"Player 2 Laps: {laps_completed_player2}", True, (0, 0, 0))
    screen.blit(laps_text_player1, (20, 20))
    screen.blit(laps_text_player2, (20, 40))

    pygame.display.flip()

pygame.quit()
