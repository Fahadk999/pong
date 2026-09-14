import pygame
from src.utils.text import Text
from src.utils.imageloader import LoadImage

class OverState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        self.centerX = self.swidth//2
        self.centerY = self.sheight//2
        self.winnerId = -1
        self.red = "#cf0c0c"
        self.blue = "#0c46cf"
        font = "assets/fonts/customfont.otf"
        timeupPath = "assets/ui/timeup.png"
        self.winnerTxt = Text("No Winner!!", self.centerX, self.centerY, font, size=30, color="white")
        self.timeupTxt = LoadImage(timeupPath, 1, swidth//2, sheight//3)

    def draw (self, screen):
        self.timeupTxt.draw(screen)
        self.winnerTxt.draw(screen)

    def update (self, dt, events, currState):
        self.timeupTxt.idleAnimationY(dt, 2, 0.075)
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                currState = "menu" 
        return currState

    def setWinnerId(self, winnerId:int)->int:
        if winnerId == 0:
            self.winnerTxt.text = "Red is the winner"
            self.winnerTxt.color = self.red
            self.winnerTxt.reRender()
        elif self.winnerId == 1:
            self.winnerTxt.text = "Blue is the winner"
            self.winnerTxt.color = self.blue
            self.winnerTxt.reRender()
    
