from PIL import Image
import pygame
import time


class GifRuner(object):
    def __init__(self, filename, scale=1):
        self.filename = filename
        self.scale = scale
        self.image = Image.open(filename)
        self.frames = []
        self.get_frames()
        self.cur = 0
        self.ptime = time.time()
        self.running = True
        self.breakpoint = len(self.frames) - 1
        self.startpoint = 0
        self.reversed = False

    def get_rect(self):
        return pygame.rect.Rect((0, 0), (self.image.size[0] * self.scale, self.image.size[1] * self.scale))

    def get_frames(self):
        image = self.image

        pal = image.getpalette()

        base_palette = []
        for i in range(0, len(pal), 3):
            rgb = pal[i:i + 3]
            base_palette.append(rgb)

        all_tiles = []
        try:
            while 1:
                if not image.tile:
                    image.seek(0)
                if image.tile:
                    all_tiles.append(image.tile[0][3][0])
                image.seek(image.tell() + 1)
        except EOFError:
            image.seek(0)

        all_tiles = tuple(set(all_tiles))

        try:
            while 1:
                try:
                    duration = image.info["duration"]
                except KeyError:
                    duration = 100

                duration *= .001  # convert to milliseconds!
                cons = False
                x0, y0, x1, y1 = (0, 0) + (image.size[0] * self.scale, image.size[1] * self.scale)
                if image.tile:
                    tile = image.tile
                else:
                    image.seek(0)
                    tile = image.tile
                if len(tile) > 0:
                    x0, y0, x1, y1 = tile[0][1]

                if all_tiles:
                    if all_tiles in ((6,), (7,)):
                        cons = True
                        pal = image.getpalette()
                        palette = []
                        for i in range(0, len(pal), 3):
                            rgb = pal[i:i + 3]
                            palette.append(rgb)
                    elif all_tiles in ((7, 8), (8, 7)):
                        pal = image.getpalette()
                        palette = []
                        for i in range(0, len(pal), 3):
                            rgb = pal[i:i + 3]
                            palette.append(rgb)
                    else:
                        palette = base_palette
                else:
                    palette = base_palette
                # ignoredErrors
                pi = pygame.image.frombuffer(image.tobytes(), image.size, image.mode)
                pi.set_palette(palette)
                pi = pygame.transform.scale(pi, (self.image.size[0] * self.scale, self.image.size[1] * self.scale))
                if "transparency" in image.info:
                    pi.set_colorkey(image.info["transparency"])

                self.frames.append([pi, duration])
                image.seek(image.tell() + 1)
        except EOFError as e:
            pass

    def render(self, screen, pos, transparency=255):
        if self.running:
            if time.time() - self.ptime > self.frames[self.cur][1]:
                if self.reversed:
                    self.cur -= 1
                    if self.cur < self.startpoint:
                        self.cur = self.breakpoint
                else:
                    self.cur += 1
                    if self.cur > self.breakpoint:
                        self.cur = self.startpoint

                self.ptime = time.time()
        pict = self.frames[self.cur][0]
        pict.set_alpha(transparency)
        screen.blit(pict, pos)

    def get_height(self):
        return (self.image.size[0] * self.scale, self.image.size[1] * self.scale)[1]

    def get_width(self):
        return (self.image.size[0] * self.scale, self.image.size[1] * self.scale)[0]

    def get_size(self):
        return (self.image.size[0] * self.scale, self.image.size[1] * self.scale)[0]
