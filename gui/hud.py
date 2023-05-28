from PIL import Image
from ursina import Texture, Sprite, destroy

from assets import AssetsManager, Assets
from data.option import Option
from gui.component.slot import SlotEntityType, SlotEntity
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


selector_off_unit = 0.044 * Option.ui_scale
selector_min_x = selector_off_unit * -4
selector_max_x = selector_off_unit * 3

# 30

# hotbar_position = Vec3(0, -0.456)
hotbar_position_y = -0.456


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
            z=-2,
            scale=0.054 * Option.ui_scale
        )

        for n in range(9):
            self.slots.append(SlotEntity(
                texture=item_textures[n % len(item_textures)],
                x=selector_min_x + n * selector_off_unit,
                y=hotbar_position_y,
            ))

        self.set_slot(5, SlotEntity(
            y=hotbar_position_y,
            texture=Assets.piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='piston',
        ))

        self.set_slot(6, SlotEntity(
            y=hotbar_position_y,
            texture=Assets.stick_piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='stick_piston',
        ))

        self.set_slot(7, SlotEntity(
            y=hotbar_position_y,
            texture=Assets.tnt,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='tnt',
        ))

        self.set_slot(8, SlotEntity(
            y=hotbar_position_y,
            texture=Assets.sandstone_carved,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='sandstone_carved',
        ))

        self.update_player_carried()

    def set_slot(self, n, slot_entity: SlotEntity):
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
