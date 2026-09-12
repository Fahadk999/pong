import pygame
#fix path for your text file
from src.utils.text import Text

class Button:
    def __init__ (self, x, y, width=100, height=50, text="Button", size=30):
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.baseColor = pygame.Color("#cf0c0c")
        self.hoverColor = pygame.Color("#0c46cf")
        self.color = self.baseColor
        self.text = text
        
        self.image = pygame.Surface((width, height))
        self.image.fill((self.color))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.border = pygame.Rect(x, y, width, height, width=2)
        # Text of Button
        self.text = Text(f"{text}", self.rect.centerx, self.rect.centery, size=size)
        
        self.isHovered = False
        self.scaleChange = True
        self.colorChange = True

        self.hoverWidth = width+10
        self.hoverHeight = height+10

    def draw (self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "white", self.rect, width=2)
        self.text.draw(screen)

    def hover (self, pos):
        self.isHovered = self.rect.collidepoint(pos)
        self.changeColor()
        self.changeScale()

    def changeColor (self):
        if self.colorChange and self.isHovered:
            self.color = self.hoverColor
            self.image.fill((self.color))
        else:
            self.color = self.baseColor
            self.image.fill((self.color))

    def click (self, events, function, *args) -> Any:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.isHovered:
                    return function(*args)
   
    def changeScale (self):
        if self.scaleChange:
            if self.isHovered:
                self.image = pygame.transform.scale(self.image, (self.hoverWidth, self.hoverHeight))
            else:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.rect = self.image.get_rect(center=(self.x, self.y))
