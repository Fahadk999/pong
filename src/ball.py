import pygame
import math
from random import uniform, randint
from src.effects.particles.particleEffect import ParticleEffect

class Ball (pygame.sprite.Sprite):
    def __init__ (self, swidth, sheight):
        super().__init__()
        self.color = pygame.Color("white")
        self.radius = 10
        self.speed = 12
        self.swidth = swidth
        self.sheight = sheight
        
        self.floatX = swidth/2
        self.floatY = sheight/2
        self.x = int(self.floatX)
        self.y = int(self.floatY)
        
        diameter = self.radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.effect = ParticleEffect(10, 5)
        
        self.drawSurface()
        self.direction = randint(0, 1)
        if self.direction == 0:
            self.angle = uniform(-(math.pi/4), math.pi/4)
        else:
            self.angle = uniform(math.radians(135), math.radians(225))
        
        self.moveX = (math.cos(self.angle)*self.speed)
        self.moveY = (math.sin(self.angle)*self.speed)

    def resetBall (self):
        self.speed = 12 
        self.floatX = self.swidth/2
        self.floatY = self.sheight/2
        self.rect = self.image.get_rect(center=(int(self.floatX), int(self.floatY)))

    def drawSurface (self):
        self.image.fill((0, 0, 0, 0)) 
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def draw (self, screen):
        screen.blit(self.image, self.rect)
        self.effect.draw(screen)
    
    def move (self, dt):
        self.floatX += self.moveX
        self.floatY += self.moveY
        
        self.rect.centerx = int(self.floatX)
        self.rect.centery = int(self.floatY)

        if self.rect.left <= 0:
            self.moveX = abs(self.moveX)
            self.floatX = self.radius
        elif self.rect.left >= self.swidth:
            self.moveX = -abs(self.moveX)
            self.floatX = self.swidth-self.radius
        if self.rect.top <= 0:
            self.moveY = abs(self.moveY)
            self.floatY = self.radius
        if self.rect.bottom >= self.sheight:
            self.moveY = -abs(self.moveY)
            self.floatY = self.sheight-self.radius
        self.effect.update(dt, self.rect.centerx, self.rect.centery, 180-math.degrees(self.angle), 10, 140, 0.15)


    def changeAngle (self, newAngle):
        self.angle = newAngle
