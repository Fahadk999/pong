from src.utils.imageloader import LoadImage

class MenuState:
    def __init__ (self, swidth, sheight):
        self.swidth, self.sheight = swidth, sheight
        titlePath = "assets/ui/pong.png"

        self.titleImg = LoadImage(titlePath, 1, swidth//2, sheight//3)
    
    def draw (self, screen):
        self.titleImg.draw(screen)

    def update (self, dt):
        self.titleImg.idleAnimationY(dt, 2, 0.075)
# click = particle
    
