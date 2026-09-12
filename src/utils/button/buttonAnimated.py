import pygame
from .buttonStd import ButtonStd
from animationManager.spriteAnimator import AnimatedSprite

class ButtonAnimated(ButtonStd):
    def __init__ (self, x, y, imgPaths, scale=1.0):
        self.buttonAnim = AnimatedSprite(x, y, imgPaths, scale, loop=True)
        super().__init__(x, y, self.buttonAnim.image.get_width(), self.buttonAnim.image.get_height())

        self.rect = self.buttonAnim.rect
        self.spriteGroup = pygame.sprite.Group(self.buttonAnim)

    def update (self, dt):
        self.spriteGroup.update()

    def draw (self, screen):
        self.spriteGroup.draw(screen)

