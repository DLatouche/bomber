from constants import Direction, FPS
from game import Game
import pygame
pygame.init()

# Define clock
clock = pygame.time.Clock()

# Create game window
logo = pygame.image.load("assets/logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Bomberman")
screen = pygame.display.set_mode((1000, 1000))

# Load game
game = Game(screen)

# Run the window
running = True
while running:

    # Clear screen
    screen.fill((0, 0, 0))

    # Load player
    screen.blit(game.player.image, game.player.rect)

    # check key used
    # top deplacement
    if game.pressed.get(pygame.K_z):
        game.player.move(Direction.TOP)
    # right deplacement
    elif game.pressed.get(pygame.K_d):
        game.player.move(Direction.RIGHT)
    # bottom deplacement
    elif game.pressed.get(pygame.K_s):
        game.player.move(Direction.BOTTOM)
    # left deplacement
    elif game.pressed.get(pygame.K_q):
        game.player.move(Direction.LEFT)

    # Update screen
    pygame.display.flip()

    # Check window event
    for event in pygame.event.get():
        # Check if event it's close
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Check keybord event
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    # fix nb FPS
    clock.tick(FPS)
