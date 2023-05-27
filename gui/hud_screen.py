from enum import Enum, auto

from PIL import Image
from ursina import Texture, Sprite, destroy, Vec3

from assets import AssetsManager, Assets
from data.option import Option
from gui.component.ui_element import UIElement

gui_image = Image.open('images/gui/widgets.png')

hotbar_texture = Texture(gui_image.crop((0, 0, 182, 22)))
hotbar_selector_texture = Texture(gui_image.crop((0, 22, 24, 46)))

# inventory

item_textures = [
    AssetsManager.get_items_image('carrot'),
    'images/blocks/torch_on',
    AssetsManager.get_items_image('iron_sword'),
    AssetsManager.get_items_image('iron_pickaxe'),
    AssetsManager.get_items_image('iron_axe'),
    AssetsManager.get_items_image('apple'),
    AssetsManager.get_items_image('arrow'),
    AssetsManager.get_items_image('bone'),
    AssetsManager.get_items_image('bucket_water'),
]


# items = os.listdir(AssetsManager.get_items_image(''))


class SlotEntityType(Enum):
    ITEM = auto(),
    BLOCK = auto(),

    def is_item(self):
        return self is SlotEntityType.ITEM

    def is_block(self):
        return self is SlotEntityType.BLOCK

    def get_scale(self) -> float:
        if self.is_item():
            return 0.035
        elif self.is_block():
            return 0.022

    def get_rotation(self) -> Vec3:
        if self is SlotEntityType.ITEM:
            return Vec3(0, 0, 0)
        elif self is SlotEntityType.BLOCK:
            return Vec3(-15, 45, 15)


selector_off_unit = 0.0444 * Option.ui_scale
selector_min_x = selector_off_unit * -4
selector_max_x = selector_off_unit * 3

# 30

hotbar_position = Vec3(0, -2.05, 4)


class SlotEntity(UIElement):
    def __init__(self, **kwargs):
        super().__init__(
            texture=Assets.apple,
            model='dropping',
            x=selector_min_x,
            y=-0.456,
            scale=SlotEntityType.ITEM.get_scale() * Option.ui_scale,
        )

        self.entity_type = SlotEntityType.ITEM
        self.identifier = 'block'

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def entity_type(self):
        return self.type

    @entity_type.setter
    def entity_type(self, entity_type: SlotEntityType):
        self.type = entity_type
        self.update_transform()

    def update_transform(self):
        self.scale = Option.ui_scale * self.type.get_scale()
        self.rotation = self.type.get_rotation()


class HotbarUI:

    def __init__(self):

        # SlotEntity
        self.slots = []
        self.slot_index = 0

        self.hotbar = UIElement(
            texture=hotbar_texture,
            y=-0.456,
            scale=0.0486 * Option.ui_scale,
        )

        self.selector = UIElement(
            texture=hotbar_selector_texture,
            x=selector_min_x,
            y=-0.456,
            scale=0.054 * Option.ui_scale
        )

        for n in range(9):
            self.slots.append(SlotEntity(
                texture=item_textures[n],
                x=selector_min_x + n * selector_off_unit,
            ))

        self.set_slot(5, SlotEntity(
            texture=Assets.piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='piston',
        ))

        self.set_slot(6, SlotEntity(
            texture=Assets.tnt,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
        ))

        self.set_slot(7, SlotEntity(
            texture=Assets.grass,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK
        ))

        self.set_slot(8, SlotEntity(
            texture=Assets.sandstone_carved,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK
        ))

        self.update_player_carried()

    def set_slot(self, n, slot_entity: SlotEntity):
        destroy(self.slots[n])
        self.slots[n] = slot_entity
        self.slots[n].x = selector_min_x + n * selector_off_unit

    def get_selected(self) -> Sprite:
        return self.slots[self.slot_index]

    def update_player_carried(self):
        from client import client
        carried = client.player.carried
        carried.set_entity(self.get_selected())

    def move_selector(self):
        if self.slot_index >= 8:
            self.selector.x = selector_min_x
            self.slot_index = 0
        else:
            self.selector.x += selector_off_unit
            self.slot_index += 1

        self.update_player_carried()
