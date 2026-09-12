import pygame
from .buttonStd import ButtonStd
from ui.imageloader import LoadImage
from animationManage.spriteAnimator import AnimationSprite

class ButtonSprite(ButtonStd):
    def __init__(self, x, y, path, scale=1) -> None:
        self.image = LoadImage(x, y, path, scale)
        super().__init__(x, y, width=self.image.image.get_width(), height=self.image.image.get_height())
        self.scaleChange = False
        self.colorChange = False
        self.rect = self.image.rect

    def draw(self, screen: pygame.Surface) -> None:
        self.image.draw(screen)

    def update (self, dt):


