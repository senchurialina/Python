import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Square settings
x, y = 300, 200
speed = 5
size = 40

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, size, size))
    pygame.display.flip()

    clock.tick(60)  # 60 FPS
