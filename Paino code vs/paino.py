import pygame
import sys

pygame.init()
pygame.mixer.init()

# Screen
WIDTH, HEIGHT = 700, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Piano")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (150, 200, 255)

# Sounds
notes = ["C", "D", "E", "F", "G", "A", "B"]
sounds = {note: pygame.mixer.Sound(f"{note}.wav") for note in notes}

# Keys
keys = []
key_width = WIDTH // len(notes)

for i, note in enumerate(notes):
    rect = pygame.Rect(i * key_width, 0, key_width, HEIGHT)
    keys.append({"rect": rect, "note": note, "pressed": False})

clock = pygame.time.Clock()

while True:
    screen.fill(GRAY)

    # Draw keys
    for key in keys:
        color = BLUE if key["pressed"] else WHITE
        pygame.draw.rect(screen, color, key["rect"])
        pygame.draw.rect(screen, BLACK, key["rect"], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in keys:
                if key["rect"].collidepoint(event.pos):
                    sounds[key["note"]].play()
                    key["pressed"] = True

        if event.type == pygame.MOUSEBUTTONUP:
            for key in keys:
                key["pressed"] = False

    pygame.display.flip()
    clock.tick(60)
