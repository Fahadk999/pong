import pygame
from src.gamestates.playstate import PlayState
from src.gamestates.menustate import MenuState

pygame.init()

swidth, sheight = 1080, 720
screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True

# Gamestates
MENU = "menu"
PLAY = "play"
OVER = "over"
currState = MENU

menustate = MenuState(swidth, sheight)
playstate = PlayState(swidth, sheight)

running = True
while running:
    dt = clock.tick(60)/1000
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    screen.fill(pygame.Color("#121314"))

    if currState == MENU:
        currState = menustate.update(dt, events, currState)
        menustate.draw(screen)
    elif currState == PLAY:
        currState = playstate.update(events, dt, keys, currState)
        playstate.draw(screen)


    pygame.display.flip()

pygame.quit()
