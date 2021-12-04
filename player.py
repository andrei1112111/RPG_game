import pygame
from map import map1


class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.z = 0
        self.img = pygame.image.load('hero.png').convert()
        self.img.set_colorkey((0, 0, 0))
        self.hero_pos = (3, 3)
        self.move = False
        self.move_to_cords = self.hero_pos
        self.clock = 0
        self.anim = 'stand'

    def camera_center(self):
        pass

    def do_anim(self):
        pass

    def event(self):
        if self.move:
            self.move_to()

    def move_to(self):
        if self.clock == 15:
            if self.hero_pos[0] > self.move_to_cords[0]:
                self.hero_pos = (self.hero_pos[0]-1, self.hero_pos[1])
            elif self.hero_pos[0] < self.move_to_cords[0]:
                self.hero_pos = (self.hero_pos[0]+1, self.hero_pos[1])
            elif self.hero_pos[1] > self.move_to_cords[1]:
                self.hero_pos = (self.hero_pos[0], self.hero_pos[1]-1)
            elif self.hero_pos[1] < self.move_to_cords[1]:
                self.hero_pos = (self.hero_pos[0], self.hero_pos[1]+1)
            else:
                self.move = False
            self.clock = 0
        else:
            self.clock += 1

    def get_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cords = self.get_cords(event.pos)
                if cords:
                    self.move = True
                    self.move_to_cords = cords
                print(cords)
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
                        if xx < pos[0] < xx+16*3 and yy < pos[1] < yy+8*3:
                            return x, y
