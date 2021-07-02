from player import Player
import pygame


class Game:
    def __init__(self, screen):
        # Create player
        self.player = Player(self)
        self.screen = screen
        self.pressed = {}
