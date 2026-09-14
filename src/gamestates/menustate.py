import pygame
from src.utils.imageloader import LoadImage
from src.utils.button.button import Button

class MenuState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        titlePath = "assets/ui/pong.png"

        self.titleImg = LoadImage(titlePath, 1, swidth//2, sheight//3)
        self.startBtn = Button(swidth//2, sheight//2, text="Start")
    
    def draw (self, screen):
        self.titleImg.draw(screen)
        self.startBtn.draw(screen)

    def update (self, dt, events, currState, playstate):
        self.titleImg.idleAnimationY(dt, 2, 0.075)
        self.startBtn.hover(pygame.mouse.get_pos())
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.startBtn.isHovered:
                    playstate.fullReset()
                    currState = "play"
                
        return currState
        
# click = particle
    
