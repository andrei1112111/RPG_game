import pygame


def load_numbered(path, flip=False):
    r = []
    for i in range(6):
        s = pygame.image.load(f'{path}/{i}.png').convert()
        if flip:
            s = pygame.transform.flip(s, True, False)
        s.set_colorkey((0, 0, 0))
        s = pygame.transform.scale(s, (80, 96))
        r.append(s)
    return r


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


grass = pygame.image.load('data/textures/blocks/grass.png').convert()
grass.set_colorkey((0, 0, 0))
grass = pygame.transform.scale(grass, (80, 96))
grass = [grass, get_average_color(io.imread('data/textures/blocks/grass.png')[:, :, :-1])]
stones = pygame.image.load('data/textures/blocks/stones.png').convert()
stones.set_colorkey((0, 0, 0))
stones = pygame.transform.scale(stones, (80, 96))
stones = [stones, get_average_color(io.imread('data/textures/blocks/stones.png')[:, :, :-1])]
flowers = pygame.image.load('data/textures/blocks/flowers.png').convert()
flowers.set_colorkey((0, 0, 0))
flowers = pygame.transform.scale(flowers, (80, 96))
flowers = [flowers, get_average_color(io.imread('data/textures/blocks/flowers.png')[:, :, :-1])]
herb = pygame.image.load('data/textures/blocks/herb.png').convert()
herb.set_colorkey((0, 0, 0))
herb = pygame.transform.scale(herb, (80, 96))
herb = [herb, get_average_color(io.imread('data/textures/blocks/herb.png')[:, :, :-1])]
planks = pygame.image.load('data/textures/blocks/planks.png').convert()
planks.set_colorkey((0, 0, 0))
planks = pygame.transform.scale(planks, (80, 96))
planks = [planks, get_average_color(io.imread('data/textures/blocks/planks.png')[:, :, :-1])]
wood = pygame.image.load('data/textures/blocks/wood.png').convert()
wood.set_colorkey((0, 0, 0))
wood = pygame.transform.scale(wood, (80, 96))
wood = [wood, get_average_color(io.imread('data/textures/blocks/wood.png')[:, :, :-1])]
foliage = pygame.image.load('data/textures/blocks/foliage.png').convert()
foliage.set_colorkey((0, 0, 0))
foliage = pygame.transform.scale(foliage, (80, 96))
foliage = [foliage, get_average_color(io.imread('data/textures/blocks/foliage.png')[:, :, :-1])]
foliage_with_cone = pygame.image.load('data/textures/blocks/foliage_with_cone.png').convert()
foliage_with_cone.set_colorkey((0, 0, 0))
foliage_with_cone = pygame.transform.scale(foliage_with_cone, (80, 96))
foliage_with_cone = [foliage_with_cone,
                     get_average_color(io.imread('data/textures/blocks/foliage_with_cone.png')[:, :, :-1])]
grass2 = pygame.image.load('data/textures/blocks/grass2.png').convert()
grass2.set_colorkey((0, 0, 0))
grass2 = pygame.transform.scale(grass2, (80, 96))
grass2 = [grass2, get_average_color(io.imread('data/textures/blocks/grass2.png')[:, :, :-1])]
cobblestone = pygame.image.load('data/textures/blocks/cobblestone.png').convert()
cobblestone.set_colorkey((0, 0, 0))
cobblestone = pygame.transform.scale(cobblestone, (80, 96))
cobblestone = [cobblestone, get_average_color(io.imread('data/textures/blocks/cobblestone.png')[:, :, :-1])]
dirt = pygame.image.load('data/textures/blocks/dirt.png').convert()
dirt.set_colorkey((0, 0, 0))
dirt = pygame.transform.scale(dirt, (80, 96))
dirt = [dirt, get_average_color(io.imread('data/textures/blocks/dirt.png')[:, :, :-1])]
water = pygame.image.load('data/textures/blocks/water.png').convert()
water.set_colorkey((0, 0, 0))
water = pygame.transform.scale(water, (80, 96))
water = [water, get_average_color(io.imread('data/textures/blocks/water.png')[:, :, :-1])]
glass = pygame.image.load('data/textures/blocks/glass.png').convert()
glass.set_colorkey((0, 0, 0))
glass = pygame.transform.scale(glass, (80, 96))
glass.set_alpha(175)
glass = [glass, get_average_color(io.imread('data/textures/blocks/glass.png')[:, :, :-1])]
tree = pygame.image.load('data/textures/blocks/tree.png').convert()
tree.set_colorkey((0, 0, 0))
tree = pygame.transform.scale(tree, (tree.get_rect().width * 4, tree.get_rect().height * 4))
tree = [tree, get_average_color(io.imread('data/textures/blocks/tree.png')[:, :, :-1])]
house = pygame.image.load('data/textures/blocks/house.png').convert()
house.set_colorkey((0, 0, 0))
house = pygame.transform.scale(house, (house.get_rect().width * 4, house.get_rect().height * 4))
house = [house, get_average_color(io.imread('data/textures/blocks/house.png')[:, :, :-1])]
empty = pygame.image.load('data/textures/blocks/empty.png').convert()
empty.set_colorkey((0, 0, 0))
empty = pygame.transform.scale(empty, (80, 96))
empty = [empty, get_average_color(io.imread('data/textures/blocks/empty.png')[:, :, :-1])]
lamp_post = pygame.image.load('data/textures/blocks/lamp_post.png').convert()
lamp_post.set_colorkey((0, 0, 0))
lamp_post = pygame.transform.scale(lamp_post, (lamp_post.get_rect().width * 4, lamp_post.get_rect().height * 4))
lamp_post = [lamp_post, get_average_color(io.imread('data/textures/blocks/lamp_post.png')[:, :, :-1])]
street_sign = pygame.image.load('data/textures/blocks/street_sign.png').convert()
street_sign.set_colorkey((0, 0, 0))
street_sign = pygame.transform.scale(street_sign, (street_sign.get_rect().width * 4, street_sign.get_rect().height * 4))
street_sign = [street_sign, get_average_color(io.imread('data/textures/blocks/street_sign.png')[:, :, :-1])]
snowman = pygame.image.load('data/textures/blocks/snowman.png').convert()
snowman.set_colorkey((0, 0, 0))
snowman = pygame.transform.scale(snowman, (snowman.get_rect().width * 4, snowman.get_rect().height * 4))
snowman = [snowman, get_average_color(io.imread('data/textures/blocks/snowman.png')[:, :, :-1])]
dried = pygame.image.load('data/textures/blocks/dried.png').convert()
dried.set_colorkey((0, 0, 0))
dried = pygame.transform.scale(dried, (dried.get_rect().width * 4, dried.get_rect().height * 4))
dried = [dried, get_average_color(io.imread('data/textures/blocks/dried.png')[:, :, :-1])]
sign_post = pygame.image.load('data/textures/blocks/sign-post.png').convert()
sign_post.set_colorkey((0, 0, 0))
sign_post = pygame.transform.scale(sign_post, (80, 96))
sign_post = [sign_post, get_average_color(io.imread('data/textures/blocks/sign-post.png')[:, :, :-1])]
wallpaperR = pygame.image.load('data/textures/blocks/wallpaperR.png').convert()
wallpaperR.set_colorkey((0, 0, 0))
wallpaperR = pygame.transform.scale(wallpaperR, (80, 96))
wallpaperR = [wallpaperR, get_average_color(io.imread('data/textures/blocks/wallpaperR.png')[:, :, :-1])]
wallpaperL = pygame.image.load('data/textures/blocks/wallpaperL.png').convert()
wallpaperL.set_colorkey((0, 0, 0))
wallpaperL = pygame.transform.scale(wallpaperL, (80, 96))
wallpaperL = [wallpaperL, get_average_color(io.imread('data/textures/blocks/wallpaperL.png')[:, :, :-1])]
table = pygame.image.load('data/textures/blocks/table.png').convert()
table.set_colorkey((0, 0, 0))
table = pygame.transform.scale(table, (table.get_rect().width * 4, table.get_rect().height * 4))
table = [table, get_average_color(io.imread('data/textures/blocks/table.png')[:, :, :-1])]
book_shelf = pygame.image.load('data/textures/blocks/book_shelf.png').convert()
book_shelf.set_colorkey((0, 0, 0))
book_shelf = pygame.transform.scale(book_shelf, (book_shelf.get_rect().width * 4, book_shelf.get_rect().height * 4))
book_shelf = [book_shelf, get_average_color(io.imread('data/textures/blocks/table.png')[:, :, :-1])]

door1 = pygame.image.load('data/textures/blocks/door1.png').convert()
door1.set_colorkey((0, 0, 0))
door1 = pygame.transform.scale(door1, (door1.get_rect().width * 4, door1.get_rect().height * 4))
door1 = [door1, get_average_color(io.imread('data/textures/blocks/door1.png')[:, :, :-1])]

door2 = pygame.image.load('data/textures/blocks/door2.png').convert()
door2.set_colorkey((0, 0, 0))
door2 = pygame.transform.scale(door2, (door2.get_rect().width * 4, door2.get_rect().height * 4))
door2 = [door2, get_average_color(io.imread('data/textures/blocks/door2.png')[:, :, :-1])]

amogus = pygame.image.load('data/textures/blocks/amogus.png').convert()
amogus.set_colorkey((0, 0, 0))
amogus = pygame.transform.scale(amogus, (amogus.get_rect().width * 4, amogus.get_rect().height * 4))
amogus = [amogus, get_average_color(io.imread('data/textures/blocks/amogus.png')[:, :, :-1])]

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
        case 16:
            return lamp_post[0]
        case 17:
            return street_sign[0]
        case 18:
            return snowman[0]
        case 19:
            return dried[0]
        case 20:
            return sign_post[0]
        case 21:
            return wallpaperR[0]
        case 22:
            return wallpaperL[0]
        case 23:
            return table[0]
        case 24:
            return book_shelf[0]
        case 25:
            return door1[0]
        case 26:
            return door2[0]
        case 27:
            return amogus[0]
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
        case 16:
            return lamp_post[-1]
        case 17:
            return street_sign[-1]
        case 18:
            return snowman[-1]
        case 19:
            return dried[-1]
        case 20:
            return sign_post[-1]
        case 21:
            return wallpaperR[-1]
        case 22:
            return wallpaperL[-1]
        case 23:
            return table[-1]
        case 24:
            return book_shelf[-1]
        case 25:
            return door1[-1]
        case 26:
            return door2[-1]
        case 27:
            return amogus[-1]
        case 99:
            return empty[-1]
