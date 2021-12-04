import pygame

grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))
wood_img = pygame.image.load('wood.png').convert()
wood_img.set_colorkey((0, 0, 0))
wood_list_img = pygame.image.load('wood_list.png').convert()
wood_list_img.set_colorkey((0, 0, 0))


def get_texture(n):
    match n:
        case 1:
            return grass_img
        case 2:
            return wood_img
        case 3:
            return wood_list_img
