import pygame, sys
from pygame.locals import *

pygame.init()

window_main = pygame.display.set_mode((600, 500), 0 , 32)
pygame.display.set_caption('Contract#1')

grass_tile = pygame.image.load('').convert()
dirt_tile = pygame.image.load('').convert()
foliage_tile = pygame.image.load('').convert()


def less_green(surface = pygame.Surface((1, 1))):	# Micheal Scott's less red video
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(pixel.r, int(pixel.g *0.5), pixel.b))



running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window_main.fill((200, 200, 200))

    less_green(grass_tile)


    pygame.display.update()

pygame.quit()
