import pygame

class Boundry:
    def __init__ (self, swidth, sheight):
        x, y = 0, 0
        self.color = "white"
        self.rect = pygame.Rect(0, 0, swidth, sheight)
        
    def draw (self, screen):
        pygame.draw.rect(screen, self.color, self.rect, width=2)
