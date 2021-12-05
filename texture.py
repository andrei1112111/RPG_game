import pygame

doski_img = pygame.image.load('data/doski.png').convert()
doski_img.set_colorkey((0, 0, 0))
doskicover_img = pygame.image.load('data/doski_kover.png').convert()
doskicover_img.set_colorkey((0, 0, 0))
doski_imgc = pygame.image.load('data/doski.png').convert()
doski_imgc.set_colorkey((0, 0, 0))
doski_imgc.set_alpha(100)
doskicover_imgc = pygame.image.load('data/doski_kover.png').convert()
doskicover_imgc.set_colorkey((0, 0, 0))
doskicover_imgc.set_alpha(100)
glass = pygame.image.load('data/glass.png').convert()
glass.set_colorkey((0, 0, 0))
button = pygame.image.load('data/button.png').convert()
button.set_colorkey((0, 0, 0))
button2 = pygame.image.load('data/button2.png').convert()
button2.set_colorkey((0, 0, 0))
button3 = pygame.image.load('data/button3.png').convert()
button3.set_colorkey((0, 0, 0))
pipi = pygame.image.load('data/0.png').convert()
pipi.set_colorkey((0, 0, 0))


def get_texture(n):
    match n:
        case 1:
            return doski_img
        case 2:
            return doskicover_img
        case 3:
            return doski_imgc
        case 4:
            return doskicover_imgc
        case 5:
            return glass
        case 6:
            return button
        case 7:
            return button2
        case 8:
            return button3
        case 9:
            return button
        case 10:
            return pipi
