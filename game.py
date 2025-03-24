import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Run Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width = 30
player_height = 60
player_x = 50        
player_y = HEIGHT - player_height
player_speed_y = 0
gravity = 1
jump_strength = -20

# Obstacles
obstacle_width = 30
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def draw_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def generate_obstacle():
    obstacle_x = WIDTH
    obstacle_y = HEIGHT - obstacle_height
    obstacles.append([obstacle_x, obstacle_y])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == HEIGHT - player_height:
                player_speed_y = jump_strength

    # Player movement
    player_speed_y += gravity
    player_y += player_speed_y

    # Keep player on the ground
    if player_y > HEIGHT - player_height:
        player_y = HEIGHT - player_height
        player_speed_y = 0

    # Obstacle generation
    if random.randint(0, 100) < 2:  # Adjust probability for obstacle frequency
        generate_obstacle()

    # Obstacle movement and collision detection
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
        if player_x < obstacle[0] + obstacle_width and \
           player_x + player_width > obstacle[0] and \
           player_y < obstacle[1] + obstacle_height and \
           player_y + player_height > obstacle[1]:
            running = False  # Game over on collision

    # Remove off-screen obstacles and increase score
    obstacles_to_remove = []
    for obstacle in obstacles:
        if obstacle[0] < -obstacle_width:
            obstacles_to_remove.append(obstacle)
            score += 1
    for obstacle in obstacles_to_remove:
        obstacles.remove(obstacle)

    # Drawing
    screen.fill(WHITE)
    draw_player(player_x, player_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1])
    draw_score(score)

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()