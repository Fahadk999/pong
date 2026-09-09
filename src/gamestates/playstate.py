from src.midline import MidLine
from src.paddle import Paddle

class PlayState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        offsetX = swidth//50
        posY = sheight//2
        self.paddleRight = Paddle(offsetX, posY, "#cf0c0c")
        self.paddleLeft = Paddle(swidth-offsetX, posY, "#0c46cf", 1)
        self.midLine = MidLine(swidth, sheight)

    def update (self, events, dt, keys, currState):
        self.paddleRight.move(self.swidth, self.sheight)
        self.paddleLeft.move(self.swidth, self.sheight)

    def draw (self, screen):
        self.midLine.draw(screen)
        self.paddleRight.draw(screen)
        self.paddleLeft.draw(screen)

    def resetGame (self):
        pass
