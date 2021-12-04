import pygame

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900), 0, 32)
display = pygame.Surface((300, 300))
clock = pygame.time.Clock()

# map1 = [[1 for _ in range(15)] for _ in range(5)]
# map2 = [[0 for _ in range(15)] for _ in range(5)]
map1 = [[[1, 0, 1], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
# map2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

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
                                                     (100 + x * 5 + y * 5 - ((z+1) * 14)) + y_pos))  # y

    player.get_move()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
