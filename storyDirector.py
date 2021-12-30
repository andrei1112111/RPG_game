class Data:
    def __init__(self, path):
        self.file = open(f'data/story/{path}.txt').readlines()

    def next(self):
        self.file.pop(0)

    def get(self):
        return self.file[0]


class StoryDirector:
    def __init__(self):
        pass

    def check(self, pos):
        return '', 'display'
