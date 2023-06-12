
from entity.player import Player
from gui.hud import HotbarUI
from gui.inventory import InventoryUI



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
