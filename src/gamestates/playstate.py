import pygame
from src.midline import MidLine
from src.ball import Ball
from src.paddle import Paddle
from src.boundry import Boundry
from src.utils.text import Text

class PlayState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        font = "assets/fonts/customfont.otf"

        offsetX = swidth//45
        posY = sheight//2
        self.paddleRight = Paddle(offsetX, posY, "#cf0c0c")
        self.paddleLeft = Paddle(swidth-offsetX, posY, "#0c46cf", 1)
        self.midLine = MidLine(swidth, sheight)
        self.ball = Ball(swidth, sheight)
        self.boundry = Boundry(swidth, sheight)

        self.scoreLeft = 0
        self.scoreRight = 0
        self.scoreLTxt = Text(f"{self.scoreLeft}", 0, 0, font, 40)
        self.scoreRTxt = Text(f"{self.scoreRight}", 0, 0, font, 40)
        self.scoreLTxt.rect.topleft = (7,0)
        self.scoreRTxt.rect.topright = (swidth-7, 0)

        self.allSprites = pygame.sprite.Group(
            self.paddleRight,
            self.paddleLeft,
            self.ball
        )

    def update (self, events, dt, keys, currState):
        self.paddleRight.move(self.sheight, self.ball)
        self.paddleLeft.move(self.sheight, self.ball)
        self.ball.move()
        if self.checkGoal():
            self.resetGame()
        
    def draw (self, screen):
        self.midLine.draw(screen)
        self.boundry.draw(screen)
        self.allSprites.draw(screen)

        self.scoreLTxt.draw(screen)
        self.scoreRTxt.draw(screen)

    def resetGame (self):
        self.ball.resetBall()
        self.paddleRight.hits = 0
        self.paddleLeft.hits = 0

    def checkGoal (self) -> bool:
        ballX = self.ball.rect.x
        if ballX <= 0:
            self.scoreRight += 1
            self.scoreRTxt.updateText(f"{self.scoreRight}")
            self.scoreRTxt.rect.topright = (self.swidth-7, 0)
            return True
        elif ballX >= self.swidth:
            self.scoreLeft += 1
            self.scoreLTxt.updateText(f"{self.scoreLeft}")
            self.scoreLTxt.rect.topleft = (7,0)
            return True
        return False
            

