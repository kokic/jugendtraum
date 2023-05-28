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


selector_off_unit = 0.044 * Option.ui_scale
selector_min_x = selector_off_unit * -4
selector_max_x = selector_off_unit * 3

# 30

# hotbar_position = Vec3(0, -0.456)
hotbar_position_y = -0.456


class HotbarSlotEntity(UIElement):
    def __init__(self, **kwargs):
        super().__init__(
            use_ratio_scale=False,
            texture=Assets.apple,
            model='dropping',
            x=selector_min_x,
            y=hotbar_position_y,
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
        self.scale = self.type.get_scale() * Option.ui_scale
        self.rotation = self.type.get_rotation()


class HotbarUI:

    def __init__(self):

        # SlotEntity
        self.slots = []
        self.slot_index = 0

        self.hotbar = UIElement(
            texture=hotbar_texture,
            y=hotbar_position_y,
            scale=0.4 * Option.ui_scale,
        )

        self.selector = UIElement(
            texture=hotbar_selector_texture,
            x=selector_min_x,
            y=hotbar_position_y,
            scale=0.054 * Option.ui_scale
        )

        for n in range(9):
            self.slots.append(HotbarSlotEntity(
                texture=item_textures[n % len(item_textures)],
                x=selector_min_x + n * selector_off_unit,
            ))

        self.set_slot(5, HotbarSlotEntity(
            texture=Assets.piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='piston',
        ))

        self.set_slot(6, HotbarSlotEntity(
            texture=Assets.stick_piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='stick_piston',
        ))

        self.set_slot(7, HotbarSlotEntity(
            texture=Assets.tnt,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='tnt',
        ))

        self.set_slot(8, HotbarSlotEntity(
            texture=Assets.sandstone_carved,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='sandstone_carved',
        ))

        self.update_player_carried()

    def set_slot(self, n, slot_entity: HotbarSlotEntity):
        if self.slots[n]:
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
