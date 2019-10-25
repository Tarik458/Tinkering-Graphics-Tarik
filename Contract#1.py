import pygame, sys
from pygame.locals import *

pygame.init()

# Set up window
window_main = pygame.display.set_mode((600, 500), 0 , 32)
pygame.display.set_caption('Contract#1')

# Load tiles
grass_tile = pygame.image.load('Grass.png')#.convert()
#dirt_tile = pygame.image.load('').convert()
#foliage_tile = pygame.image.load('').convert()


# Less blue and green to seem slightly darker and redder like autumn.
def autumn(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(pixel.r, int(pixel.g * 0.9), int(pixel.b * 0.8)))


# More blue and less red and green so it is like puddles form.
def wet(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(int(pixel.r * 0.9), int(pixel.g * 0.9), int(pixel.b * 1.1)))


FPS = 15
FPSClock = pygame.time.Clock()
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_1]:
        autumn(grass_tile)
    if keys[K_2]:
        wet(grass_tile)

    window_main.fill((200, 200, 200))
    pygame.Surface.blit(window_main, grass_tile, (10, 10))


    FPSClock.tick(FPS)
    pygame.display.update()

pygame.quit()
