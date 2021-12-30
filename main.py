import pygame
from map import map1

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900), pygame.SRCALPHA, 32)
display = pygame.Surface((300, 300))
clock = pygame.time.Clock()

from texture import get_texture
from player import Player
from interface import MiniMap

player = Player()
minimap = MiniMap(player, pygame, display)

while True:
    clock.tick(300)
    pygame.display.set_caption(f'FPS: {round(clock.get_fps())}')

    display.fill((255, 255, 255))
    x_pos, y_pos = player.get_pos()
    len_row = len(map1[0]) - 1
    len_map = len(map1) - 1
    for y, row in enumerate(map1):
        for x, height in enumerate(row):
            for z, tile in enumerate(height):
                if tile:
                    texture_tile = get_texture(tile)
                    if z != 0 and (x == 0 or x == len_row or y == 0 or y == len_map):
                        texture_tile.set_alpha(120)
                    else:
                        texture_tile.set_alpha(255)
                    display.blit(texture_tile, ((150 + x * 10 - y * 10) + x_pos,  # X
                                         (100 + x * 5 + y * 5 - (
                                                 (z + 1) * 14)) + y_pos))  # y

    player.get_move()
    player.event()
    player.camera_center()
    display.blit(player.img, player.get_player_pos())

    minimap.display_minimap()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
