import pygame
from configparser import ConfigParser

pygame.init()

config = ConfigParser()
config.read('config.ini')

screen = pygame.display.set_mode((int(config['graphics']['width']), int(config['graphics']['height'])))
pygame.display.set_caption(config['main']['name'])


def main():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    camera = Vector2(int(config['graphics']['width']) // 2, int(config['graphics']['height']) // 2)
    player = Player((270, 180), screen, all_sprites)
    interface = Interface()
    offset = 0, 0

    event_10in_second = pygame.USEREVENT + 1
    pygame.time.set_timer(event_10in_second, 100)

    font = pygame.font.SysFont('Comic Sans MS', 30)

    storyDirector = StoryDirector()

    while True:
        screen.fill((30, 30, 30))

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
        for y, row in enumerate(island):
            for x, height in enumerate(row):
                xp = (150 + x * 40 - y * 40 + x_pos)
                if -3000 < xp < 2220:
                    for z, tile in enumerate(height):
                        if tile:
                            if not (z > player.pos_z and (sum([x, y]) >= sum([xx, yy]))):
                                yp = (100 + x * 20 + y * 20 - ((z + 1) * 56 + y_pos))
                                if -300 < yp < 1380:
                                    screen.blit(get_texture(tile), (xp, yp))

        screen.blit(player.image, player.rect.topleft + offset)

        for y, row in enumerate(island):
            for x, height in enumerate(row):
                xp = (150 + x * 40 - y * 40 + x_pos)
                if -100 < xp < 2020:
                    for z, tile in enumerate(height):
                        if tile:
                            if z > player.pos_z and (sum([x, y]) >= sum([xx, yy])):
                                yp = (100 + x * 20 + y * 20 - ((z + 1) * 56 + y_pos))
                                if -100 < yp < 1180:
                                    screen.blit(get_texture(tile), (xp, yp))
        """↓↓↓Интерфейс↓↓↓"""
        # HP
        x, y = 1860, 20
        for h in interface.get():
            screen.blit(interface.images[h], (x, y))
            x -= 50
        """↑↑↑Интерфейс↑↑↑"""

        player.correct_move(offset, (960 - camera[0], camera[1] - 540))
        pygame.display.flip()
        clock.tick(int(config['graphics']['fps']))


if __name__ == '__main__':
    from map import island
    from objects import Player
    from interface import Interface
    from pygame.math import Vector2
    from storyDirector import StoryDirector
    from load import get_texture

    main()

