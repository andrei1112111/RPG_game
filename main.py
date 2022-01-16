import pygame
from configparser import ConfigParser

from gif import GIFImage

pygame.init()

config = ConfigParser()
config.read('config.ini')

screen = pygame.display.set_mode((int(config['graphics']['width']), int(config['graphics']['height'])))
pygame.display.set_caption(config['main']['name'])


def main():
    island = Game_map()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    camera = Vector2(int(config['graphics']['width']) // 2, int(config['graphics']['height']) // 2)
    player = Player((-305, 1005), screen, island, all_sprites)
    interface = Interface()
    snowflakes = SnowWind(screen, 100, speed=5)
    offset = 0, 0

    event_10in_second = pygame.USEREVENT + 1
    pygame.time.set_timer(event_10in_second, 100)

    font = pygame.font.SysFont('Comic Sans MS', 30)

    storyDirector = StoryDirector()

    # Экран предзагрузки
    background = GIFImage("data/interface/background/gif2.gif", scale=2.2)
    pygame.font.init()
    font = pygame.font.SysFont('Trebuchet MS', 30)
    textsurface = font.render('Нажмите клавишу', False, (255, 255, 255))
    bold_font = pygame.font.SysFont('Arial Black', 30)
    bold_textsurface = bold_font.render('Enter', False, (255, 255, 255))
    transparency = 255
    smoothness = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not smoothness:
                    smoothness = True
                if event.key == pygame.K_ESCAPE:
                    exit(-2)
        screen.fill((0, 0, 0))
        background.render(screen, (int(config['graphics']['width']) // 2 - background.get_width() // 2,
                                   int(config['graphics']['height']) // 2 - background.get_height() // 2),
                          transparency=transparency)
        screen.blit(textsurface, (int(config['graphics']['width']) - 450, int(config['graphics']['height']) - 100))
        screen.blit(bold_textsurface, (int(config['graphics']['width']) - 185, int(config['graphics']['height']) - 102))
        pygame.display.flip()
        if smoothness:
            transparency -= 10
        if transparency <= 0:
            running = False
    transparency = 0
    black_background = pygame.Surface((int(config['graphics']['width']), int(config['graphics']['height'])))
    black_background.fill((33, 33, 33))
    k = 255
    while True:
        screen.fill(island.col())
        for event in pygame.event.get():
            if event.type == event_10in_second:
                events = storyDirector.check(player.pos)
                if events[1] == 'display':
                    pass

            player.handle_event(event)
        keys = pygame.key.get_pressed()
        player.pressed(keys)

        all_sprites.update(offset, (960 - camera[0], camera[1] - 540))

        heading = player.pos - camera
        camera += heading * 0.05
        offset = -1 * camera + Vector2(int(config['graphics']['width']) // 2,
                                       int(config['graphics']['height']) // 2)

        x = round((player.pos[0] - 140) // 40)
        y = round((player.pos[1] - 20) // 20)
        xx = ((-(((x + 1) - y) - 1)) // 2) + 1
        yy = ((x + y) // 2)
        x_pos, y_pos = 960 - camera[0], camera[1] - 540
        for y, row in enumerate(island.ret()):
            for x, height in enumerate(row):
                xp = (150 + x * 40 - y * 40 + x_pos)
                if -600 < xp < 1920:
                    for z, tile in enumerate(height):
                        if tile:
                            if not (z > player.pos_z and (sum([x, y]) >= sum([xx, yy]))):
                                yp = (100 + x * 20 + y * 20 - ((z + 1) * 56 + y_pos))
                                if -600 < yp < 1080:
                                    screen.blit(get_texture(tile, player.snow_k), (xp, yp))

        screen.blit(player.image, player.rect.topleft + offset)

        for y, row in enumerate(island.ret()):
            for x, height in enumerate(row):
                xp = (150 + x * 40 - y * 40 + x_pos)
                if 0 < xp < 1920:
                    for z, tile in enumerate(height):
                        if tile:
                            if z > player.pos_z and (sum([x, y]) >= sum([xx, yy])):
                                yp = (100 + x * 20 + y * 20 - ((z + 1) * 56 + y_pos))
                                if 0 < yp < 1080:
                                    screen.blit(get_texture(tile, player.snow_k), (xp, yp))

        """↓↓↓Cнежинки↓↓↓"""
        if not island.k:
            snowflakes.display(heading)  # <-- плавность сдвига снежинок
        """↑↑↑Cнежинки↑↑↑"""

        """↓↓↓Интерфейс↓↓↓"""
        x, y = 1860, 20
        for h in interface.get():
            screen.blit(interface.images[h], (x, y))
            x -= 50
        """↑↑↑Интерфейс↑↑↑"""

        player.correct_move(offset, (960 - camera[0], camera[1] - 540))
        screen.set_alpha(transparency)
        if player.obuch_mg:
            screen.blit(player.obuch_mg, (1920//2, 1080//2))
        if k:
            black_background.set_alpha(k)
            screen.blit(black_background, (0, 0))
            k -= int(((k / 255) ** -1) * 10)
            if k <= 0:
                k = None
        pygame.display.flip()
        clock.tick(int(config['graphics']['fps']))


if __name__ == '__main__':
    from map import Game_map
    from objects import Player
    from interface import Interface, SnowWind
    from pygame.math import Vector2
    from storyDirector import StoryDirector
    from load import get_texture

    main()
