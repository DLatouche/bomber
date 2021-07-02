from player import Player
import pygame
pygame.init()

# Create game window
pygame.display.set_caption("Bomberman", "/assets/bomber.png")
screen = pygame.display.set_mode((1000, 1000))

# Run the window
running = True
while running:

    # Check window event
    for event in pygame.event.get():
        # Check if event it's close
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
