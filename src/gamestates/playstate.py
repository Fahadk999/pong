import pygame
from src.midline import MidLine
from src.ball import Ball
from src.paddle import Paddle

class PlayState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        offsetX = swidth//50
        posY = sheight//2
        self.paddleRight = Paddle(offsetX, posY, "#cf0c0c")
        self.paddleLeft = Paddle(swidth-offsetX, posY, "#0c46cf", 1)
        self.midLine = MidLine(swidth, sheight)
        self.ball = Ball(swidth, sheight)

        self.allSprites = pygame.sprite.Group()

    def update (self, events, dt, keys, currState):
        self.paddleRight.move(self.sheight, self.ball)
        self.paddleLeft.move(self.sheight, self.ball)
        self.ball.move()

    def draw (self, screen):
        self.midLine.draw(screen)
        self.paddleRight.draw(screen)
        self.paddleLeft.draw(screen)
        self.ball.draw(screen)

    def resetGame (self):
        pass
