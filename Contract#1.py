## Contract One ##
## -Tarik Sabin ##
import pygame, sys
from pygame.locals import *

pygame.init()

# Set up window.
window_main = pygame.display.set_mode((600, 500), 0 , 32)
pygame.display.set_caption('Contract#1')

# Load tile png.
grass_tile = pygame.image.load('Grass.png').convert()


# decreased blue and green to seem slightly darker and more red/brown like autumn.
def autumn(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(pixel.r, int(pixel.g * 0.9), int(pixel.b * 0.8)))


# increased blue and decreased red and green so it is like puddles form.
def wet(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(int(pixel.r * 0.9), int(pixel.g * 0.9), int(pixel.b * 1.1)))


# Increased red and decreased blue to make it look more yellow and dry.
def dried(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(int(pixel.r * 1.1), pixel.g, int(pixel.b * 0.9)))

# FPS clock stops values of colour from changing too quickly.
FPS = 15
FPSClock = pygame.time.Clock()

running = True

# Main loop
while running == True:
    # Quit checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Checks if a key has been pressed and calls the relevant function.
    keys = pygame.key.get_pressed()
    if keys[K_1]:
        autumn(grass_tile)
    if keys[K_2]:
        wet(grass_tile)
    if keys[K_3]:
        dried(grass_tile)

    # Drawing and updating of window.
    window_main.fill((200, 200, 200))
    pygame.Surface.blit(window_main, grass_tile, (10, 10))
    FPSClock.tick(FPS)
    pygame.display.update()

pygame.quit()
