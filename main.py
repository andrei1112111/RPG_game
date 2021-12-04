import pygame
from map import map1

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900), pygame.SRCALPHA, 32)
display = pygame.Surface((300, 300))
clock = pygame.time.Clock()

from texture import get_texture
from player import Player

player = Player()

while True:
    clock.tick(60)
    pygame.display.set_caption(f'FPS: {clock.get_fps()}')

    display.fill((0, 0, 0))
    x_pos, y_pos = player.get_pos()
    for y, row in enumerate(map1):
        for x, height in enumerate(row):
            for z, tile in enumerate(height):
                if tile:
                    display.blit(get_texture(tile), ((150 + x * 10 - y * 10) + x_pos,  # X
                                                     (100 + x * 5 + y * 5 - ((z + 1) * 14)) + y_pos))  # y

    player.get_move()
    player.event()
    player.camera_center()
    display.blit(player.img, player.get_player_pos())

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
