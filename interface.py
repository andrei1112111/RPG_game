import time

import numpy as np
from map import map1
from texture import get_mini_texture
from pygame import gfxdraw


class MiniMap:
    def __init__(self, player, pygame, display):
        self.display = display
        self.player = player
        self.pygame = pygame
        self.size = 200
        self.position = [10, 10]
        self.border_color = pygame.Color('gray')
        self.mapping = []
        for x in map1:
            buffer_2 = []
            for y in x:
                buffer_3 = [0, 0, 0]
                for z in reversed(y):
                    if z != 0:
                        obj = get_mini_texture(z)
                        buffer_3 = [
                            int(obj[0]),
                            int(obj[1]),
                            int(obj[2])
                        ]
                        break
                buffer_2.append(buffer_3)
            self.mapping.append(buffer_2)

    def get_around_player_mapping(self):
        around_player_mapping = []
        limit_x = len(self.mapping)
        limit_y = len(self.mapping[0])
        for x_color in range(self.player.hero_pos[1] - 20, self.player.hero_pos[1] + 20):
            buffer = []
            for y_color in range(self.player.hero_pos[0] - 20, self.player.hero_pos[0] + 20):
                if 0 <= x_color < limit_x and 0 <= y_color < limit_y:
                    buffer.append(self.mapping[x_color][y_color])
                else:
                    buffer.append([0, 0, 0])
            around_player_mapping.append(buffer)
        return around_player_mapping

    def display_minimap(self):
        fast_display = self.display
        apm = self.get_around_player_mapping()
        for index_y, yy in enumerate(apm):
            for index_x, color in enumerate(yy):
                fast_display.set_at((self.position[0] + index_x, self.position[1] + index_y), color)
        poses_board = [
            self.position[0],
            self.position[0],
            40,
            40
        ]
        poses_player = [
            self.position[0] + 20,
            self.position[0] + 20,
            1,
            1
        ]
        self.pygame.draw.rect(self.display, self.border_color, poses_board, width=1)
        self.pygame.draw.rect(self.display, self.pygame.Color('white'), poses_player)
