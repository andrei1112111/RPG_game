import pygame
from map import map1


class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.z = 0
        self.img = pygame.image.load('data/hero.png').convert()
        self.img.set_colorkey((0, 0, 0))
        self.hero_pos = (3, 4)
        self.move = False
        self.move_to_cords = self.hero_pos
        self.clock = 0
        self.clock2 = 0
        self.anim = ('stand', None, None)
        self.anim_list = []
        self.event_anim = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_anim, 2000)

    def camera_center(self):
        pass

    def do_anim(self):
        print(self.anim[0])
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
                        self.anim = ('stand', None, None)
                        print('СОБЫТИЕ')

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
        if self.clock == 15:
            if self.hero_pos[0] > self.move_to_cords[0]:
                self.hero_pos = (self.hero_pos[0] - 1, self.hero_pos[1])
            elif self.hero_pos[0] < self.move_to_cords[0]:
                self.hero_pos = (self.hero_pos[0] + 1, self.hero_pos[1])
            elif self.hero_pos[1] > self.move_to_cords[1]:
                self.hero_pos = (self.hero_pos[0], self.hero_pos[1] - 1)
            elif self.hero_pos[1] < self.move_to_cords[1]:
                self.hero_pos = (self.hero_pos[0], self.hero_pos[1] + 1)
            else:
                self.move = False
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
                    self.move = True
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
