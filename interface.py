from configparser import ConfigParser
from itertools import chain, cycle
import pygame

config = ConfigParser()
config.read('config.ini')


def load_interface():
    res = []
    for i in range(2):
        img = pygame.image.load(f'data/interface/heart/{i}.png').convert()
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.scale(img, (40, 32))
        res.append(img)
    for i in range(3):
        img = pygame.image.load(f'data/interface/training/e/{i}.png').convert()
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.scale(img, (40, 32))
        res.append(img)
    return res


class Interface:
    def __init__(self):
        self.maxHP = int(config['difficulty']['maxHP'])
        self.healPoints = int(config['difficulty']['defaultHP'])
        self.images = load_interface()
        self.menu = None

    def get(self):
        return list(chain([1 for _ in range(self.healPoints)],
                          [0 for _ in range(self.maxHP - self.healPoints)]))

    def damage(self):
        """Игрок получил урон"""
        if self.healPoints > 1:
            self.healPoints -= 1
        else:
            return True  # смерть

    def heal(self):
        """Игрок приобрел здоровье"""
        if self.healPoints <= self.maxHP:
            self.healPoints += 1
        else:
            return True  # HP максимален

    def training(self, key):
        pass
