from configparser import ConfigParser
from itertools import chain, cycle
import pygame
import random

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


class SnowWind:
    def __init__(self, screen, number_snowflakes=0, speed=1, k=0.06):
        self.screen = screen
        self.snowflakes = []
        self.number_snowflakes = number_snowflakes
        self.width = int(config['graphics']['width'])
        self.height = int(config['graphics']['height'])
        self.speed = speed
        self.k = k
        for _ in range(number_snowflakes):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            self.snowflakes.append([x, y])
        self.snowflake_color = pygame.Color('gray')

    def display(self, moving):
        moving = -moving
        for index_flake in range(self.number_snowflakes):
            pygame.draw.circle(self.screen, self.snowflake_color, self.snowflakes[index_flake], 3)
            self.snowflakes[index_flake][1] += self.speed
            self.snowflakes[index_flake] += (moving * self.k)
            if self.snowflakes[index_flake][1] > self.height:
                y = random.randrange(0, 50)
                self.snowflakes[index_flake][1] = -y
                x = random.randrange(0, self.width)
                self.snowflakes[index_flake][0] = x
            if self.snowflakes[index_flake][1] < 0:
                y = random.randrange(self.height + 0, self.height + 50)
                self.snowflakes[index_flake][1] = y
                x = random.randrange(0, self.width)
                self.snowflakes[index_flake][0] = x
            if self.snowflakes[index_flake][0] < 0:
                y = random.randrange(0, self.height)
                self.snowflakes[index_flake][1] = y
                x = random.randrange(self.width + 0, self.width + 50)
                self.snowflakes[index_flake][0] = x
            if self.snowflakes[index_flake][0] > self.width:
                y = random.randrange(0, self.height)
                self.snowflakes[index_flake][1] = y
                x = random.randrange(0, 50)
                self.snowflakes[index_flake][0] = -x
