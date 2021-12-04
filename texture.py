import pygame

grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))


def get_texture(n):
    if n == 1:
        return grass_img
