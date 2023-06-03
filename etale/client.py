from enum import Enum, auto

from entity.player import Player
from gui.hud import HotbarUI
from gui.inventory import InventoryUI


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
        self.player: Player = None
        self.player_operation_blocked: bool = False

        self.inventory_ui: InventoryUI = None
        self.hotbar_ui: HotbarUI = None

    def load(self):
        # TODO: hotbar will use player carried entity currently [rewrite]
        self.player: Player = Player()

        self.inventory_ui = InventoryUI()
        # self.inventory_ui.disable()

        self.hotbar_ui = HotbarUI()


client = Client()
