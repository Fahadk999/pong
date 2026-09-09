import pygame

class MidLine:
    def __init__ (self, swidth, sheight):
        self.color = pygame.Color("#242424")
        self.width = 5
        self.image = pygame.Surface((self.width, sheight))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(swidth//2, sheight//2))

    def draw (self, screen):
        screen.blit(self.image, self.rect)
