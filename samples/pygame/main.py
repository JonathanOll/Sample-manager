import pygame
from settings import *
from time import time
import sys


# setup
pygame.init()
clock = pygame.time.Clock()

# game

class Game:

    def __init__(self, screen):

        self.screen = screen
        self.closing_request = False

    def paint(self):
        
        self.screen.fill("black")

    def update(self, dt):

        if self.closing_request:
            pygame.quit()
            sys.exit()

    def handle_events(self, events):
        pass
        # handle events

    def close(self):
        self.closing_request = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Window")
# if SOUND_ENABLED:
#     pygame.mixer.Sound("assets/sounds/music.wav").play()

game = Game(screen)
last_tick = time()

while True:

    dt = time() - last_tick
    last_tick = time()

    events = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game.close()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                DEBUG = not DEBUG
        else:
            events.append(event)

    game.handle_events(events)
    
    if MAX_DT > 0 and dt > MAX_DT:
        continue

    game.update(dt)
    game.paint()

    clock.tick(FPS)
