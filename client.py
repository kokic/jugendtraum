from enum import Enum, auto

from entity.player import Player


class ViewDirection(Enum):
    TOP = auto(),
    BOTTOM = auto(),
    LEFT = auto()
    RIGHT = auto()
    FRONT = auto()
    BACK = auto()

    def top(self):
        return self is ViewDirection.TOP

    def bottom(self):
        return self is ViewDirection.BOTTOM

    def left(self):
        return self is ViewDirection.LEFT

    def right(self):
        return self is ViewDirection.RIGHT

    def front(self):
        return self is ViewDirection.FRONT

    def back(self):
        return self is ViewDirection.BACK


def get_face_from_normal(normal):
    normal = round(normal)

    if normal == (0, 1, 0):
        return ViewDirection.TOP

    elif normal == (0, -1, 0):
        return ViewDirection.BOTTOM

    elif normal == (-1, 0, 0):
        return ViewDirection.LEFT

    elif normal == (1, 0, 0):
        return ViewDirection.RIGHT

    elif normal == (0, 0, -1):
        return ViewDirection.FRONT

    elif normal == (0, 0, 1):
        return ViewDirection.BACK


class Client:

    def __init__(self):
        self.__player: Player = None

    @property
    def player(self):
        if not self.__player:
            self.__player = Player()
        return self.__player


client = Client()
