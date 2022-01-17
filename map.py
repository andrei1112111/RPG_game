import ast


def load(name):
    with open(f'{name}.txt', mode='r') as f:
        return ast.literal_eval(f.readlines()[0])


homee = load('data/home')
island = load('data/land')


class Game_map:
    def __init__(self):
        self.k = 0

    def ret(self):
        if self.k:
            return homee
        else:
            return island

    def col(self):
        if self.k:
            return (33, 33, 33)
        else:
            return (240, 240, 240)
