from typing import Any

import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 2
        self.image = 