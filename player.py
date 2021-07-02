from constants import Direction
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 5
        self.nb_bomb = 1
        self.life = 1
        self.image = pygame.image.load('./assets/player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def move(self, direction):
        if direction == Direction.TOP and self.rect.y > 0:
            self.rect.y -= self.velocity
        elif direction == Direction.RIGHT and self.rect.x + self.rect.width < self.game.screen.get_width():
            self.rect.x += self.velocity
        elif direction == Direction.BOTTOM and self.rect.y + self.rect.height < self.game.screen.get_height():
            self.rect.y += self.velocity
        elif direction == Direction.LEFT and self.rect.x > 0:
            self.rect.x -= self.velocity
