import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__ (self, x, y, color, id=0):
        self.id = id
        self.speed = 5
        self.color = pygame.Color(color)
        self.x, self.y = x, y
        self.width, self.height = 30, 100
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))
        
    def move (self, swidth, sheight):
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
        self.rect.bottom = min(sheight-self.rect.height, self.rect.bottom)

    def draw (self, screen):
        screen.blit(self.image, self.rect)

