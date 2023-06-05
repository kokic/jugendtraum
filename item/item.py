from ursina import Entity

from assets import Assets
from gui.component.slot import SlotData, SlotEntityType


class ItemInstance(Entity):
    pass


class Item:
    items = {}

    @staticmethod
    def register_item(identifier, item):
        item.identifier = identifier
        Item.items[identifier] = item

    def __init__(self, texture=Assets.empty):
        self.texture = texture
        self.identifier = 'item'

    def use_on(self, instance, data, target: Entity):
        pass

