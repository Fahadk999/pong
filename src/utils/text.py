import pygame
# from abs_path import absPath

class Text:
    def __init__(self, text, posX, posY, font=None, size=48, color=pygame.Color("white")):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.text = str(text)
        
        self.font = pygame.font.Font(font, size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.posX, self.posY))
        self.fixedX = self.rect.x
        self.glow = False
        self.glowTimer = 0
        self.glowInterval = 300

    def draw (self, screen):
        screen.blit(self.surface, self.rect)

    def enableGlow (self):
        self.glow = True

    def updateText (self, text):
        self.surface = self.font.render(str(text), True, self.color)
        self.rect = self.surface.get_rect(center=(self.posX, self.posY))
        self.adjust()

    def updatePox (self, newX=0, newY=0):
        self.rect = self.surface.get_rect(center=(newX, newY))

    def makeGlow (self, dt, glowColor="yellow"):
        if self.glow:
            if self.glowTimer <= self.glowInterval:
                self.glowTimer += dt
                self.color = pygame.Color(glowColor)
                self.surface = self.font.render(self.text, True, self.color)
            else:
                self.glowTimer = 0
                self.color = pygame.Color("white")
                self.surface = self.font.render(self.text, True, self.color)
                self.glow = False

    def adjust (self):
        self.rect.x = self.fixedX+self.rect.width//2
            
