import pygame


class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def get_move(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y_pos += 1
        elif keys[pygame.K_s]:
            self.y_pos -= 1

    def get_pos(self):
        return self.x_pos, self.y_pos
