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
        self.maxDeflection = 45
        self.hits = 0
        self.hitLimit = 4

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
            self.hits += 1
            hitX = other.rect.x
            hitY = other.rect.y
            padLenHalf = self.height//2
            collideDist = max(-padLenHalf, min(other.rect.centery-self.rect.centery, padLenHalf))
            percentage = collideDist/padLenHalf

            if self.id == 0:
                angle = math.radians(self.maxDeflection*percentage) 
                other.moveX = (math.cos(angle)*other.speed)
                other.moveY = (math.sin(angle)*other.speed)
                other.floatX = hitX+other.radius
                other.floatX = self.rect.right+other.radius

            if self.id == 1:
                angle = math.radians(180-(self.maxDeflection*percentage))
                other.moveX = (math.cos(angle)*other.speed)
                other.moveY = (math.sin(angle)*other.speed)
                other.floatX = self.rect.left-other.radius

            other.rect.centerx = int(other.floatX)
            if self.hits >= self.hitLimit:
                other.speed += 1
                self.hits = 0
