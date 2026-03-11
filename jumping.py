import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Example")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Sounds
sound = pygame.mixer.Sound("Sounds/click.wav")

# Rectangle
rect = pygame.Rect(250, 150, 100, 100)
rect_color = RED

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                sound.play()
                # Toggle color when clicked
                rect_color = GREEN if rect_color == RED else RED

    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
