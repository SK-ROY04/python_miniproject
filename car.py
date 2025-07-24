import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Car Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Car settings
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10

# Obstacle settings
obstacle_width = 50
obstacle_height = 80
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Clock
clock = pygame.time.Clock()

def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_width, car_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

# Main game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basic AI: Move left/right to avoid obstacle
    if obstacle_y > 200:
        if car_x + car_width < obstacle_x:
            car_x += 5
        elif car_x > obstacle_x + obstacle_width:
            car_x -= 5

    # Move obstacle
    obstacle_y += obstacle_speed

    # Respawn obstacle
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)

    # Draw
    draw_car(car_x, car_y)
    draw_obstacle(obstacle_x, obstacle_y)
    pygame.display.update()

pygame.quit()
