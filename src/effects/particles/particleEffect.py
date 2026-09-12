import pygame
from .particle import Particle
from random import uniform

# timer is in seconds
class ParticleEffect:
    def __init__ (self, speed, count):
        self.particleGroup = pygame.sprite.Group()
        self.count = count
        self.speed = speed
        self.timer = 0
        self.maxTime = 0.055
        self.spawnTimer = uniform(0, self.maxTime)

    def update (self, dt, x, y, dirAngle, angleOffset, speed, timeAlive):
        self.timer += dt
        if self.timer >= self.spawnTimer:
            self.spawnParticle(x, y, dirAngle, angleOffset, speed, timeAlive)
            self.timer = 0
            self.spawnTimer = uniform(0, self.maxTime)
        self.particleGroup.update(dt)
        
    def spawnParticle (self, x, y, dirAngle, angleOffset, speed, timeAlive):
        for c in range(0, self.count):
            self.particleGroup.add(Particle(x, y, dirAngle, angleOffset, speed, timeAlive))

    def draw (self, screen):
        self.particleGroup.draw(screen)

