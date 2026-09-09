import pygame
from src.gamestates.playstate import PlayState

pygame.init()

swidth, sheight = 1080, 720
screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True

# Gamestates
playstate = PlayState(swidth, sheight)

running = True
while running:
    dt = clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    playstate.update(events, dt, keys, "PLAY")
    screen.fill(pygame.Color("#121314"))
    playstate.draw(screen)

    pygame.display.flip()

pygame.quit()
