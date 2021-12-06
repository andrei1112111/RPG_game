import pygame

grass = pygame.image.load('data/textures/grass.png').convert()
grass.set_colorkey((0, 0, 0))
stones = pygame.image.load('data/textures/stones.png').convert()
stones.set_colorkey((0, 0, 0))
flowers = pygame.image.load('data/textures/flowers.png').convert()
flowers.set_colorkey((0, 0, 0))
herb = pygame.image.load('data/textures/herb.png').convert()
herb.set_colorkey((0, 0, 0))
planks = pygame.image.load('data/textures/planks.png').convert()
planks.set_colorkey((0, 0, 0))
wood = pygame.image.load('data/textures/wood.png').convert()
wood.set_colorkey((0, 0, 0))
foliage = pygame.image.load('data/textures/foliage.png').convert()
foliage.set_colorkey((0, 0, 0))
foliage_with_cone = pygame.image.load('data/textures/foliage_with_cone.png').convert()
foliage_with_cone.set_colorkey((0, 0, 0))


def get_texture(n):
    match n:
        case 1:
            return grass
        case 2:
            return stones
        case 3:
            return flowers
        case 4:
            return herb
        case 5:
            return planks
        case 6:
            return wood
        case 7:
            return foliage
        case 8:
            return foliage_with_cone


