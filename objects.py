import pygame

from load import load_numbered
from pygame.math import Vector2
from itertools import cycle as infinite_cycle


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, mapp, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.image = pygame.image.load('data/textures/characters/diluc/stands/0.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (80, 96))
        self.rect = self.image.get_rect(center=pos)
        self.collisons_block1 = pygame.Rect(0, 0, 42, 46)
        self.collisons_block2 = pygame.Rect(0, 0, 84, 23)
        self.collisons_player = pygame.Rect(0, 0, 24, 8)
        self.pos = Vector2(pos)
        self.pos_z = 0
        self.vel = Vector2(0, 0)
        self.frame_animation = infinite_cycle([0, 1, 2, 3, 4, 5])
        self.event_10in_second = pygame.USEREVENT + 1
        self.event_stand = pygame.USEREVENT + 2
        self.event_check = pygame.USEREVENT + 3
        pygame.time.set_timer(self.event_check, 500)
        self.run_front = load_numbered('data/textures/characters/diluc/runs_f2f')
        self.run_right = load_numbered('data/textures/characters/diluc/runs_side')
        self.run_back = load_numbered('data/textures/characters/diluc/runs_back')
        self.run_left = load_numbered('data/textures/characters/diluc/runs_side', True)
        self.run_stand = load_numbered('data/textures/characters/diluc/stands')
        self.run_snow = load_numbered('data/textures/characters/diluc/digging', True)
        self.move = None
        self.home_able = False
        self.un_home_able = False
        self.obuch_mg = None
        self.botton_e = [pygame.image.load('data/interface/training/e/0.png').convert(),
                         pygame.image.load('data/interface/training/e/1.png').convert(),
                         pygame.image.load('data/interface/training/e/2.png').convert(),
                         pygame.image.load('data/interface/training/e/3.png').convert(),
                         pygame.image.load('data/interface/training/e/4.png').convert(),
                         pygame.image.load('data/interface/training/e/5.png').convert()]
        [i.set_colorkey((255, 255, 255)) for i in self.botton_e]
        self.botton_e = [pygame.transform.scale(i, (80, 96)) for i in self.botton_e]
        self.k = 0
        self.mapp = mapp
        self.snow_k = 0

    def get_cords(self):
        x = round((self.pos[0] - 140) // 40)
        y = round((self.pos[1] - 20) // 20)
        xx = ((-(((x + 1) - y) - 1)) // 2) + 1
        yy = ((x + y) // 2)
        return xx, yy

    def check(self):
        x, y = self.get_cords()
        xh, yh = 41, 10
        if (x + 1 == xh or x - 1 == xh or x == xh) and (y + 1 == yh or y - 1 == yh or y == yh):
            self.obuch_mg = self.botton_e[self.k]
            if self.k == 5:
                self.k = 0
            else:
                self.k += 1
            self.home_able = True
        elif (x + 1 == 1 or x - 1 == 1 or x == 1) and (y + 1 == 7 or y - 1 == 7 or y == 7):
            self.obuch_mg = self.botton_e[self.k]
            if self.k == 5:
                self.k = 0
            else:
                self.k += 1
            self.un_home_able = True
        elif (x + 1 == 50 or x - 1 == 50 or x == 50) and (y + 1 == 12 or y - 1 == 12 or y == 12):
            self.obuch_mg = self.botton_e[self.k]
            if pygame.key.get_pressed()[pygame.K_e]:
                if self.snow_k <= 7:
                    self.snow_k += 1
        elif (x + 1 == 2 or x - 1 == 2 or x == 2) and (y + 1 == 3 or y - 1 == 3 or y == 3):
            return 'les'
        else:
            self.obuch_mg = None
            self.home_able = self.un_home_able = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.vel.x = 5
                pygame.time.set_timer(self.event_stand, 0)
            elif event.key == pygame.K_a:
                self.vel.x = -5
                pygame.time.set_timer(self.event_stand, 0)
            elif event.key == pygame.K_w:
                self.vel.y = -5
                pygame.time.set_timer(self.event_stand, 0)
            elif event.key == pygame.K_s:
                self.vel.y = 5
                pygame.time.set_timer(self.event_stand, 0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.vel.x > 0:
                self.vel.x = 0
                self.move = None
                pygame.time.set_timer(self.event_stand, 2000)
            elif event.key == pygame.K_a and self.vel.x < 0:
                self.vel.x = 0
                self.move = None
                pygame.time.set_timer(self.event_stand, 2000)
            elif event.key == pygame.K_w:
                self.vel.y = 0
                self.move = None
                pygame.time.set_timer(self.event_stand, 2000)
            elif event.key == pygame.K_s:
                self.vel.y = 0
                self.move = None
                pygame.time.set_timer(self.event_stand, 2000)
        if event.type == self.event_stand:
            self.move = 'st'
        if event.type == self.event_10in_second:
            if self.move == 'st':
                fr = self.frame_animation.__next__()
                self.image = self.run_stand[fr]
            elif self.move == 's':
                fr = self.frame_animation.__next__()
                self.image = self.run_front[fr]
            elif self.move == 'd':
                fr = self.frame_animation.__next__()
                self.image = self.run_right[fr]
            elif self.move == 'w':
                fr = self.frame_animation.__next__()
                self.image = self.run_back[fr]
            elif self.move == 'a':
                fr = self.frame_animation.__next__()
                self.image = self.run_left[fr]
            elif self.move == 'snow':
                fr = self.frame_animation.__next__()
                self.image = self.run_snow[fr]
            else:
                self.image = pygame.image.load('data/textures/characters/diluc/stands/0.png').convert()
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (80, 96))
        if event.type == self.event_check:
            return self.check()

    def pressed(self, key):
        if key[pygame.K_ESCAPE]:
            exit(-2)
        if key[pygame.K_w]:
            self.move = 'w'
        elif key[pygame.K_s]:
            self.move = 's'
        elif key[pygame.K_a]:
            self.move = 'a'
        elif key[pygame.K_d]:
            self.move = 'd'
        elif key[pygame.K_e] and 1 <= self.snow_k <= 7:
            self.move = 'snow'
        if key[pygame.K_f]:
            print(self.pos)
            print(self.get_cords(), '-----------------------')
        if key[pygame.K_e]:
            if self.home_able:
                self.mapp.k = 1
                self.pos = Vector2(425, 180)
                self.rect = self.image.get_rect(center=self.pos)
            elif self.un_home_able:
                self.mapp.k = 0
                self.pos = Vector2(-1005, 1045)
                self.rect = self.image.get_rect(center=self.pos)

    def correct_move(self, offset, pos):
        """Пройдет ли игрок сквозь текстуры или по воздуху"""
        r = [False]
        self.collisons_player.topleft = (
            self.rect.topleft[0] + offset[0] + self.vel.x + 32, self.rect.topleft[1] + offset[1] + self.vel.y + 88)
        for y, row in enumerate(self.mapp.ret()):
            for x, height in enumerate(row):
                xp = (150 + x * 40 - y * 40 + pos[0])
                if -100 < xp < 2020:
                    for z, tile in enumerate(height):
                        if z == self.pos_z and tile and (not self.mapp.ret()[y][x][z + 1]):
                            yp = (100 + x * 20 + y * 20 - ((z + 1) * 56 + pos[1]))
                            if -100 < yp < 1180:
                                # вертикальный квадрат
                                self.collisons_block1.topleft = (xp - 1 + 20, yp - 1)
                                # pygame.draw.rect(self.screen, (255, 0, 0), self.collisons_block1, 1)
                                # pygame.draw.rect(self.screen, (255, 255, 0), self.collisons_player, 1)
                                r.append(self.collisons_block1.contains(self.collisons_player))
                                # горизонтальный квадрат
                                self.collisons_block2.topleft = (xp - 2, yp + 11)
                                # pygame.draw.rect(self.screen, (0, 0, 255), self.collisons_block2, 1)
                                r.append(self.collisons_block2.contains(self.collisons_player))

        return any(r)

    def update(self, offset, pos):
        # Передвижение
        if self.correct_move(offset, pos):
            self.pos += self.vel
            self.rect.center = self.pos
