import pygame


class Data:
    def __init__(self, path):
        self.file = open(f'data/story/{path}.txt').readlines()

    def next(self):
        self.file.pop(0)

    def get(self):
        return self.file[0]


class StoryDirector:
    def __init__(self):
        self.n = 0
        self.mg = pygame.image.load('data/textures/dialog/4.png').convert()

    def check(self, k, home):
        if home and self.n == 0:
            self.mg = pygame.image.load('data/textures/dialog/3.png').convert()
            self.n += 1
        elif k == 8 and self.n == 1:
            self.mg = pygame.image.load('data/textures/dialog/2.png').convert()
            self.n += 1
        elif k == 9:
            self.mg = pygame.image.load('data/textures/dialog/1.png').convert()

    def get(self, k):
        if k == 1:
            return pygame.image.load('data/textures/dialog/0.png').convert()
        else:
            return self.mg

    def get_img(self):
        return self.mg
