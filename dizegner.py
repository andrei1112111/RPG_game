import datetime
import os
from itertools import cycle

import pygame

CELL_SIZE = 40
X_SIZE = 75
Y_SIZE = 45
view_x, view_y = 10, 10
Z_SIZE = 32

INDEX_MAP = [[[0 for _ in range(Z_SIZE)] for _ in range(Y_SIZE)] for _ in range(X_SIZE)]

TEXTURE_INDEX_MAP = {
    'data/textures/blocks/grass.png': 1,
    'data/textures/blocks/flowers.png': 3,
    'data/textures/blocks/foliage_with_cone.png': 8,
    'data/textures/blocks/foliage.png': 7,
    'data/textures/blocks/wood.png': 6,
    'data/textures/blocks/herb.png': 4,
    'data/textures/blocks/stones.png': 2,
    'data/textures/blocks/AIR.png': 0,
    'data/textures/blocks/planks.png': 5,
    'data/textures/blocks/grass2.png': 9,
    'data/textures/blocks/cobblestone.png': 10,
    'data/textures/blocks/dirt.png': 11,
    'data/textures/blocks/water.png': 12,
    'data/textures/blocks/glass.png': 13,
    'data/textures/blocks/tree.png': 14,
    'data/textures/blocks/house.png': 15,
    'data/textures/blocks/lamp_post.png': 16,
    'data/textures/blocks/street_sign.png': 17,
    'data/textures/blocks/snowman.png': 18,
    'data/textures/blocks/dried.png': 19,
    'data/textures/blocks/sign-post.png': 20,
    'data/textures/blocks/wallpaperR.png': 21,
    'data/textures/blocks/wallpaperL.png': 22,
    'data/textures/blocks/table.png': 23,
    'data/textures/blocks/book_shelf.png': 24,
    'data/textures/blocks/door1.png': 25,
    'data/textures/blocks/door2.png': 26,
    'data/textures/blocks/amogus.png': 27,
    'data/textures/blocks'
    '/0.png': 28,
    'data/textures/blocks/empty.png': 99,
}
try:
    from map import island as map1
    with open(f'backups/backup-{datetime.datetime.now().strftime("%Y-%m-%d %H-%M")}.txt', mode='w') as f:
        f.write(str(map1))
    existing_map = map1
except ImportError:
    existing_map = None


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Texture(pygame.sprite.Sprite):
    def __init__(self, file_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert(),
                                            (CELL_SIZE - 3, CELL_SIZE - 3))
        self.file_path = file_path
        self.rect = self.image.get_rect()
        self.texture_index = TEXTURE_INDEX_MAP[file_path]


class Board:
    def __init__(self, width, height, all_sprites, view_x=False, view_y=False):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = CELL_SIZE
        self.cells = []
        self.cells_matrix = []
        self.all_sprites = all_sprites
        self.current_view_X, self.current_view_Y = [0, 0]
        self.current_point_X, self.current_point_Y = [0, 0]
        self.myfont = pygame.font.SysFont('Times New Romans', 18)
        if view_x:
            self.view_x = view_x
        else:
            self.view_x = width
        if view_y:
            self.view_y = view_y
        else:
            self.view_y = height

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def load(self, ex_map):
        global INDEX_MAP
        INDEX_MAP = ex_map
        self.cells_matrix = [[[0 for _ in range(Z_SIZE)] for _ in range(Y_SIZE)] for _ in range(X_SIZE)]
        for x_index, x in enumerate(list(reversed(ex_map))):
            for y_index, y in enumerate(x):
                clrs = cycle(self.all_sprites)
                new_current_texture = next(clrs)
                upper_texture = None
                texture_level_index = 0
                for index, z in list(reversed(list(enumerate(y)))):
                    if z != 0:
                        upper_texture = z
                        texture_level_index = index
                        break
                if upper_texture:
                    for key in TEXTURE_INDEX_MAP.keys():
                        if TEXTURE_INDEX_MAP[key] == upper_texture:
                            while new_current_texture.file_path != key:
                                new_current_texture = next(clrs)
                            self.cells_matrix[x_index][y_index] = [clrs, new_current_texture, texture_level_index]
                else:
                    self.cells_matrix[x_index][y_index] = [clrs, new_current_texture, texture_level_index]

    def render(self, screen):
        for x in range(self.current_view_X, self.current_view_X + self.view_x):
            buffer = []
            for y in range(self.current_view_Y, self.current_view_Y + self.view_y):
                sss = [self.left + self.cell_size * (x - self.current_view_X),
                       self.top + self.cell_size * (y - self.current_view_Y), self.cell_size,
                       self.cell_size]
                if len(self.cells) < self.width * self.height:
                    self.cells.append(
                        [[self.left + self.cell_size * x, self.top + self.cell_size * y,
                          self.left + self.cell_size * x + self.cell_size,
                          self.left + self.cell_size * y + self.cell_size], [x, y]])
                    clrs = cycle(self.all_sprites)
                    buffer.append([clrs, next(clrs), 0])
                pygame.draw.rect(screen, pygame.Color('gray'), sss, width=1)
            if len(self.cells_matrix) < self.width:
                self.cells_matrix.append(buffer)
        sss = [self.left + self.cell_size * (self.current_point_X - self.current_view_X),
               self.top + self.cell_size * (self.current_point_Y - self.current_view_Y), self.cell_size,
               self.cell_size]
        pygame.draw.rect(screen, pygame.Color('red'), sss, width=4)

        for x in range(self.current_view_X, self.view_x + self.current_view_X):
            for y in range(self.current_view_Y, self.current_view_Y + self.view_y):
                sss = (1 + self.left + self.cell_size * (x - self.current_view_X),
                       1 + self.top + self.cell_size * (y - self.current_view_Y))
                textr = self.cells_matrix[x][y][1]
                textr.rect.topleft = sss
                # buffer_sprites = pygame.sprite.Group()
                # buffer_sprites.add(textr)
                # buffer_sprites.draw(screen)
                screen.blit(textr.image, sss)
                textsurface = self.myfont.render(str(self.cells_matrix[x][y][-1]), False,
                                                 (210, 210, 210))
                screen.blit(textsurface, sss)

    def get_cell(self, mouse_pos):
        flag = True
        for recc in self.cells:
            if recc[0][0] <= mouse_pos[0] <= recc[0][2] and recc[0][1] <= mouse_pos[1] <= recc[0][
                -1]:
                flag = False
                return recc[-1][0], recc[-1][-1]
        if flag:
            return None

    def on_click(self, cell, reverse):
        if cell and not reverse:
            self.cells_matrix[cell[0]][cell[-1]][1] = next(self.cells_matrix[cell[0]][cell[-1]][0])
        else:
            for _ in range(len(self.all_sprites) - 1):
                self.cells_matrix[cell[0]][cell[-1]][1] = next(
                    self.cells_matrix[cell[0]][cell[-1]][0])

    def get_click(self, plus=False, reverse=False):
        cell = self.current_point_X, self.current_point_Y
        self.on_click(cell, reverse)

    def change_layer(self, plus):
        cell = self.current_point_X, self.current_point_Y
        if plus and self.cells_matrix[cell[0]][cell[-1]][-1] < Z_SIZE:
            self.cells_matrix[cell[0]][cell[-1]][-1] += 1
        elif not plus and self.cells_matrix[cell[0]][cell[-1]][-1] > 0:
            self.cells_matrix[cell[0]][cell[-1]][-1] -= 1

    def save(self):
        for xi, line in enumerate(list(reversed(self.cells_matrix))):
            for yi, cell in enumerate(line):
                if INDEX_MAP[xi][yi][cell[2]] == 0:
                    INDEX_MAP[xi][yi][cell[2]] = cell[1].texture_index
        print('Saved')

    def printing(self):
        with open(f'map.py', mode='w') as f:
            f.write('island = ' + str(INDEX_MAP))
        print('Writed.')
        # clipboard.copy(str(INDEX_MAP))
        # print('Copied into buffer...')

    def dot_save(self):
        cell = self.cells_matrix[self.current_point_X][self.current_point_Y]
        if INDEX_MAP[abs(self.current_point_X - (X_SIZE - 1))][self.current_point_Y][cell[2]] == 0:
            INDEX_MAP[abs(self.current_point_X - (X_SIZE - 1))][self.current_point_Y][cell[2]] = \
                cell[1].texture_index
            print(f'saved x-{self.current_point_X} y-{self.current_point_Y}')
            return
        print('Error')
        return

    def delete_dot(self):
        cell = self.cells_matrix[self.current_point_X][self.current_point_Y]
        INDEX_MAP[abs(self.current_point_X - (X_SIZE - 1))][self.current_point_Y][cell[2]] = 0
        print('deleted')

    def p_up(self):
        if 0 <= self.current_point_Y - 1 <= Y_SIZE - 1:
            self.current_point_Y -= 1

    def p_down(self):
        if 0 <= self.current_point_Y + 1 <= Y_SIZE - 1:
            self.current_point_Y += 1

    def p_left(self):
        if 0 <= self.current_point_X - 1 <= X_SIZE - 1:
            self.current_point_X -= 1

    def p_right(self):
        if 0 <= self.current_point_X + 1 <= X_SIZE - 1:
            self.current_point_X += 1

    def v_up(self):
        if 0 <= self.current_view_Y - 1 <= Y_SIZE - 1:
            self.current_view_Y -= 1
            self.current_point_Y -= 1

    def v_down(self):
        if 0 <= self.current_view_Y + 1 <= Y_SIZE - 1:
            self.current_view_Y += 1
            self.current_point_Y += 1

    def v_left(self):
        if 0 <= self.current_view_X - 1 <= X_SIZE - 1:
            self.current_view_X -= 1
            self.current_point_X -= 1

    def v_right(self):
        if 0 <= self.current_view_X + 1 <= X_SIZE - 1:
            self.current_view_X += 1
            self.current_point_X += 1


def check():
    if view_x > X_SIZE or view_y > Y_SIZE:
        print(BColors.FAIL + "Внимание: Параметр величины обзора не может быть больше размера карты!")
        exit(-2)


def main():
    check()
    pygame.init()
    screen = pygame.display.set_mode((view_x * CELL_SIZE + 20, view_y * CELL_SIZE + 20))
    pygame.display.set_caption('DIZIGNER')
    all_sprites = pygame.sprite.Group()
    buffer_textures = []
    for d, dirs, files in os.walk('data/textures/blocks/'):
        for f in files:
            buffer_textures.append(str(d + f))
    switch = 14
    buffer_textures[switch], buffer_textures[0] = buffer_textures[0], buffer_textures[switch]
    for fil in buffer_textures:
        fileT = Texture(fil)
        all_sprites.add(fileT)

    board = Board(X_SIZE, Y_SIZE, all_sprites, view_x=view_x, view_y=view_y)
    running = True
    clock = pygame.time.Clock()
    if existing_map:
        board.load(existing_map)
    while running:
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board.get_click()
                if event.key == pygame.K_DOWN:
                    board.get_click(reverse=True)
                if event.key == pygame.K_SPACE:
                    board.dot_save()
                if event.key == pygame.K_DELETE:
                    board.delete_dot()
                if event.key == pygame.K_e:
                    board.change_layer(plus=False)
                if event.key == pygame.K_q:
                    board.change_layer(plus=True)
                if event.key == pygame.K_w:
                    board.p_up()
                if event.key == pygame.K_s:
                    board.p_down()
                if pygame.key.get_mods() and pygame.KMOD_CTRL:
                    if event.key == pygame.K_s:
                        board.save()
                if event.key == pygame.K_a:
                    board.p_left()
                if event.key == pygame.K_d:
                    board.p_right()

                if event.key == pygame.K_i:
                    board.v_up()
                if event.key == pygame.K_k:
                    board.v_down()
                if event.key == pygame.K_j:
                    board.v_left()
                if event.key == pygame.K_l:
                    board.v_right()

                if event.key == pygame.K_p:
                    if pygame.key.get_mods() and pygame.KMOD_CTRL:
                        board.printing()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
