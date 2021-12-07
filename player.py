import pygame
from map import map1
from runTo import pers_go_to


class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.z = 0
        self.img = pygame.image.load('data/characters/diluc/stands/0.png').convert()
        self.img.set_colorkey((0, 0, 0))
        self.hero_pos = (0, 0)
        self.hero_pos0 = self.hero_pos
        self.move = []
        self.move_to_cords = self.hero_pos
        self.clock = 0
        self.clock2 = 0
        self.anim = ('none', [], [])
        self.anim_list = []
        self.event_anim = pygame.USEREVENT + 1
        self.eblock = False
        pygame.time.set_timer(self.event_anim, 1500)

    def check_interaction(self):
        if not self.eblock:
            if map1[self.hero_pos[0]][self.hero_pos[1]][self.z + 2] == 10:
                self.anim = ('ch_block', [[0, 1, 2], [0, 1, 3], [0, 2, 2], [0, 2, 3]], 3)
                self.eblock = True

    def camera_center(self):
        if self.hero_pos != self.hero_pos0:
            k = -1
            if self.hero_pos[1] != self.hero_pos0[1]:
                if self.hero_pos[1] > self.hero_pos0[1]:
                    k = 1
                self.x_pos += -10 * -k
                self.y_pos += 4 * -k
            else:
                if self.hero_pos[0] > self.hero_pos0[0]:
                    k = 1
                self.x_pos += -10 * k
                self.y_pos += -4 * k

            self.hero_pos0 = self.hero_pos

    def do_anim(self):
        # print(self.anim[0])
        match self.anim[0]:
            case 'button':
                if [self.hero_pos[0], self.hero_pos[1], self.z + 1] == self.anim[1]:
                    if self.anim[2] == 1:
                        map1[self.hero_pos[0]][self.hero_pos[1]][self.z + 1] = 7
                        self.anim = [self.anim[0], self.anim[1], 2]
                    elif self.anim[2] == 2:
                        map1[self.hero_pos[0]][self.hero_pos[1]][self.z + 1] = 8
                        self.anim = [self.anim[0], self.anim[1], 3]
                    elif self.anim[2] == 3:
                        map1[self.hero_pos[0]][self.hero_pos[1]][self.z + 1] = 9
                        self.anim = ('ch_block', [[0, 1, 2], [0, 1, 3], [0, 2, 2], [0, 2, 3]], 3)
                else:
                    map1[self.anim[1][0]][self.anim[1][1]][self.anim[1][2]] = 6
                    self.anim = ('none', [], [])
            case 'ch_block':
                for dot in self.anim[1]:
                    map1[dot[0]][dot[1]][dot[2]] = self.anim[2]
                self.eblock = False
                self.anim = ('none', [], [])

    def get_bottom(self):
        return map1[self.hero_pos[0]][self.hero_pos[1]][self.z + 1]

    def event(self):
        if self.move:
            self.move_to()
        else:
            match self.get_bottom():
                case 6:
                    self.anim = 'button', [self.hero_pos[0], self.hero_pos[1], self.z + 1], 1

    def move_to(self):
        # print(self.hero_pos)
        if self.clock == 15:
            if self.move:
                to = self.move.pop(0)
                match to:
                    case 'down':
                        self.hero_pos = (self.hero_pos[0], self.hero_pos[1] + 1)
                    case 'up':
                        self.hero_pos = (self.hero_pos[0], self.hero_pos[1] - 1)
                    case 'left':
                        self.hero_pos = (self.hero_pos[0] - 1, self.hero_pos[1])
                    case 'right':
                        self.hero_pos = (self.hero_pos[0] + 1, self.hero_pos[1])
        self.clock += 1
        if self.clock == 16:
            self.clock = 0

    def get_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cords = self.get_cords(event.pos)
                if cords:
                    self.move = pers_go_to(self.hero_pos, cords)
                    self.move_to_cords = cords
            if event.type == self.event_anim:
                self.do_anim()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y_pos += 1
        elif keys[pygame.K_s]:
            self.y_pos -= 1
        if keys[pygame.K_a]:
            self.x_pos += 1
        elif keys[pygame.K_d]:
            self.x_pos -= 1
        elif keys[pygame.K_e]:
            self.check_interaction()

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_player_pos(self):
        return ((150 + self.hero_pos[0] * 10 - self.hero_pos[1] * 10) + self.x_pos,
                (100 + self.hero_pos[0] * 5 + self.hero_pos[1] * 5 - ((self.z + 2) * 14)) + self.y_pos)

    def get_cords(self, pos):
        for y, row in enumerate(map1):
            for x, height in enumerate(row):
                for z, tile in enumerate(height):
                    if z == self.z and tile:
                        xx = (((150 + x * 10 - y * 10) + self.x_pos) * 3)
                        yy = (((100 + x * 5 + y * 5 - ((z + 1) * 14)) + self.y_pos) * 3)
                        if xx < pos[0] < xx + 16 * 3 and yy < pos[1] < yy + 8 * 3:
                            return x, y
