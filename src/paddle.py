import pygame
from random import uniform
import math

class Paddle(pygame.sprite.Sprite):
    def __init__ (self, x, y, color, id=0):
        super().__init__()
        self.id = id
        self.speed = 15
        self.color = pygame.Color(color)
        self.x, self.y = x, y
        self.width, self.height = 30, 100
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))
        
    def move (self, sheight, other):
        keys = pygame.key.get_pressed()

        dy = 0
        if self.id == 0:
            if keys[pygame.K_w]:
                dy -= self.speed
            elif keys[pygame.K_s]:
                dy += self.speed
        elif self.id == 1:
            if keys[pygame.K_UP]:
                dy -= self.speed
            elif keys[pygame.K_DOWN]:
                dy += self.speed

        self.rect.y += dy
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(sheight, self.rect.bottom)
        self.collide(other)

    def draw (self, screen):
        screen.blit(self.image, self.rect)

    def collide (self, other):
        if self.rect.colliderect(other.rect):
            hitX = other.rect.x
            hitY = other.rect.y

            if self.id == 0:
                maxA, minA = 45, -45
                randAngle = uniform(math.radians(minA), math.radians(maxA))
                other.moveX = (math.cos(randAngle)*other.speed)
                other.moveY = (math.sin(randAngle)*other.speed)
                other.floatX = hitX+other.radius
                other.floatX = self.rect.right+other.radius

            if self.id == 1:
                maxA, minA = 135, 315
                randAngle = uniform(math.radians(minA), math.radians(maxA))
                other.moveX = (math.cos(randAngle)*other.speed)
                other.moveY = (math.sin(randAngle)*other.speed)
                other.floatX = self.rect.left-other.radius

            other.rect.centerx = int(other.floatX)


                

