import math

from PIL import Image
from ursina import Texture, Vec3

from assets import Assets
from data.option import Option
from gui.component.ui_element import UIElement
from gui.hud import SlotEntity, SlotEntityType

inventory_image = Image.open('images/gui/container/inventory.png')
# window_image = Image.open('images/gui/window.png')


inventory_texture = Texture(inventory_image.crop((0, 0, 176, 166)))
# window_texture = Texture(window_image.crop((0, 0, 252, 140)))


slot_off_unit = 0.0358 * Option.ui_scale
slot_min_x = slot_off_unit * -4
slot_max_x = slot_off_unit * 3

slot_min_y = -0.018 * Option.ui_scale


class InventoryUI(UIElement):

    def __init__(self):
        super().__init__(texture=inventory_texture, scale=0.35 * Option.ui_scale)
        # self.z = -1

        # 27
        self.slots = []

        for n in range(0, 13):
            self.slots.append(SlotEntity(
                texture=Assets.carrot,
                x=slot_min_x + n % 9 * slot_off_unit,
                y=slot_min_y - n // 9 * slot_off_unit,
                ratio=1.1
            ))

        for n in range(13, 27):
            self.slots.append(SlotEntity(
                texture=Assets.piston,
                model=Assets.block,
                x=slot_min_x + n % 9 * slot_off_unit,
                y=slot_min_y - n // 9 * slot_off_unit,
                entity_type=SlotEntityType.BLOCK,
                ratio=1.1
            ))
