import pygame
from skimage import io


def get_average_color(mapp):
    r, g, b = 0, 0, 0
    counter = 0
    for line in mapp:
        for elem in line:
            if elem[0] != 0 or \
                    elem[1] != 0 or \
                    elem[-1] != 0:
                counter += 1
                r += int(elem[0])
                g += elem[1]
                b += elem[-1]
    if counter != 0:
        return [int(r / counter), int(g / counter), int(b / counter)]
    else:
        return [255, 255, 255]


grass = pygame.image.load('data/textures/grass.png').convert()
grass.set_colorkey((0, 0, 0))
grass = [grass, get_average_color(io.imread('data/textures/grass.png')[:, :, :-1])]
stones = pygame.image.load('data/textures/stones.png').convert()
stones.set_colorkey((0, 0, 0))
stones = [stones, get_average_color(io.imread('data/textures/stones.png')[:, :, :-1])]
flowers = pygame.image.load('data/textures/flowers.png').convert()
flowers.set_colorkey((0, 0, 0))
flowers = [flowers, get_average_color(io.imread('data/textures/flowers.png')[:, :, :-1])]
herb = pygame.image.load('data/textures/herb.png').convert()
herb.set_colorkey((0, 0, 0))
herb = [herb, get_average_color(io.imread('data/textures/herb.png')[:, :, :-1])]
planks = pygame.image.load('data/textures/planks.png').convert()
planks.set_colorkey((0, 0, 0))
planks = [planks, get_average_color(io.imread('data/textures/planks.png')[:, :, :-1])]
wood = pygame.image.load('data/textures/wood.png').convert()
wood.set_colorkey((0, 0, 0))
wood = [wood, get_average_color(io.imread('data/textures/wood.png')[:, :, :-1])]
foliage = pygame.image.load('data/textures/foliage.png').convert()
foliage.set_colorkey((0, 0, 0))
foliage = [foliage, get_average_color(io.imread('data/textures/foliage.png')[:, :, :-1])]
foliage_with_cone = pygame.image.load('data/textures/foliage_with_cone.png').convert()
foliage_with_cone.set_colorkey((0, 0, 0))
foliage_with_cone = [foliage_with_cone,
                     get_average_color(io.imread('data/textures/foliage_with_cone.png')[:, :, :-1])]
grass2 = pygame.image.load('data/textures/grass2.png').convert()
grass2.set_colorkey((0, 0, 0))
grass2 = [grass2, get_average_color(io.imread('data/textures/grass2.png')[:, :, :-1])]
cobblestone = pygame.image.load('data/textures/cobblestone.png').convert()
cobblestone.set_colorkey((0, 0, 0))
cobblestone = [cobblestone, get_average_color(io.imread('data/textures/cobblestone.png')[:, :, :-1])]
dirt = pygame.image.load('data/textures/dirt.png').convert()
dirt.set_colorkey((0, 0, 0))
dirt = [dirt, get_average_color(io.imread('data/textures/dirt.png')[:, :, :-1])]
water = pygame.image.load('data/textures/water.png').convert()
water.set_colorkey((0, 0, 0))
water = [water, get_average_color(io.imread('data/textures/water.png')[:, :, :-1])]
glass = pygame.image.load('data/textures/glass.png').convert()
glass.set_colorkey((0, 0, 0))
glass.set_alpha(200)
glass = [glass, get_average_color(io.imread('data/textures/glass.png')[:, :, :-1])]
tree = pygame.image.load('data/textures/tree.png').convert()
tree.set_colorkey((0, 0, 0))
tree = [tree, get_average_color(io.imread('data/textures/tree.png')[:, :, :-1])]
house = pygame.image.load('data/textures/house.png').convert()
house.set_colorkey((0, 0, 0))
house = [house, get_average_color(io.imread('data/textures/house.png')[:, :, :-1])]
empty = pygame.image.load('data/textures/empty.png').convert()
empty.set_colorkey((0, 0, 0))
empty = [empty, get_average_color(io.imread('data/textures/empty.png')[:, :, :-1])]


def get_texture(n):
    match n:
        case 1:
            return grass[0]
        case 2:
            return stones[0]
        case 3:
            return flowers[0]
        case 4:
            return herb[0]
        case 5:
            return planks[0]
        case 6:
            return wood[0]
        case 7:
            return foliage[0]
        case 8:
            return foliage_with_cone[0]
        case 9:
            return grass2[0]
        case 10:
            return cobblestone[0]
        case 11:
            return dirt[0]
        case 12:
            return water[0]
        case 13:
            return glass[0]
        case 14:
            return tree[0]
        case 15:
            return house[0]
        case 99:
            return empty[0]


def get_mini_texture(n):
    match n:
        case 1:
            return grass[-1]
        case 2:
            return stones[-1]
        case 3:
            return flowers[-1]
        case 4:
            return herb[-1]
        case 5:
            return planks[-1]
        case 6:
            return wood[-1]
        case 7:
            return foliage[-1]
        case 8:
            return foliage_with_cone[-1]
        case 9:
            return grass2[-1]
        case 10:
            return cobblestone[-1]
        case 11:
            return dirt[-1]
        case 12:
            return water[-1]
        case 13:
            return glass[-1]
        case 14:
            return tree[-1]
        case 15:
            return house[-1]
        case 99:
            return empty[-1]
