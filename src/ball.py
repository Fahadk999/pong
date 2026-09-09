import pygame
import random
import math

class Ball (pygame.sprite.Sprite):
    def __init__ (self, swidth, sheight):
        super().__init__()
        self.color = pygame.Color("white")
        self.radius = 10
        self.speed = 1
        
        # 1. Store the true center position as floating-point decimals
        self.float_x = swidth / 2
        self.float_y = sheight / 2
        
        diameter = self.radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(int(self.float_x), int(self.float_y)))
        
        self.drawSurface()
        tx = swidth
        ty = 0
        dx = tx - self.rect.centerx
        dy = ty - self.rect.centery
        dist = math.hypot(dx, dy)
        
        self.moveX = ((dx/dist)*self.speed)
        self.moveY = ((dy/dist)*self.speed)

    def drawSurface (self):
        self.image.fill((0, 0, 0, 0)) 
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def draw (self, surface):
        surface.blit(self.image, self.rect)
    
    def move (self):
        # 2. Add the decimals to your floating-point trackers
        self.float_x += self.moveX
        self.float_y += self.moveY
        
        # 3. Update the rect position with the tracked coordinates
        self.rect.centerx = int(self.float_x)
        self.rect.centery = int(self.float_y)
