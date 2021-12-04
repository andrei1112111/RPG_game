import pygame
from map import map1


class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.img = pygame.image.load('hero.png').convert()
        self.img.set_colorkey((0, 0, 0))

    def get_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.get_cords(event.pos))
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

    def get_cords(self, pos):
        for y, row in enumerate(map1):
            for x, height in enumerate(row):
                for z, tile in enumerate(height):
                    if tile == 1:
                        xx = (((150 + x * 10 - y * 10) + self.x_pos) * 3)
                        yy = (((100 + x * 5 + y * 5 - ((z + 1) * 14)) + self.y_pos) * 3)
                        if xx < pos[0] < xx+20*3 and yy < pos[1] < yy+10*3:
                            return x, y
