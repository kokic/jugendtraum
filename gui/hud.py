from PIL import Image
from ursina import Texture, Vec3, curve, Func

from assets import AssetsManager, Assets
from data.option import Option
from data.shared import Shared
from gui.component.slot import SlotEntityType, SlotEntity, SlotData
from gui.component.ui_element import UIElement

gui_image = Image.open('images/gui/widgets.png')

hotbar_texture = Texture(gui_image.crop((0, 0, 182, 22)))
hotbar_selector_texture = Texture(gui_image.crop((0, 22, 24, 46)))


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
        self.selector_index = 0

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

        # TODO: load items from inventory
        self.create_slots()

        # self.debug_set_slots()

        self.update_player_carried()

    def debug_set_slots(self):
        pass

    def create_slots(self):
        from etale.client import client
        hotbar_slots = client.inventory_ui.hotbar_slots
        for n in range(len(hotbar_slots)):
            slot = SlotEntity(
                x=selector_min_x + n * selector_off_unit,
                y=hotbar_position_y,
            )
            hotbar_slots[n].get_data().set_data_to(slot)
            self.slots.append(slot)

    def set_slot(self, n, data: SlotData = SlotData.empty):
        data.set_data_to(self.slots[n])

        if self.selector_index == n:
            self.update_player_carried()

    def get_selected_data(self) -> SlotData:
        return self.slots[self.selector_index].get_data()

    def update_player_carried(self):
        from etale.client import client
        from entity.carried import CarriedItem

        carried = client.player.carried
        base_position = CarriedItem.get_base_position(carried.entity_type)
        target_position = CarriedItem.get_base_position(self.get_selected_data().entity_type)

        seq = carried.animate_position(
            value=base_position - Vec3(0, Shared.carried_down_offset, 0),
            duration=Shared.carried_up_animation_duration,
            curve=curve.linear
        )[1]
        seq.append(Func(lambda: self.get_selected_data().set_data_to(client.player.carried)))
        seq.append(Func(lambda: carried.animate_position(
            value=target_position,
            duration=Shared.carried_down_animation_duration,
            curve=curve.linear
        )))

    def move_selector(self, offset=1):
        real_offset = (self.selector_index + offset) % 9 - self.selector_index
        self.selector.x += selector_off_unit * real_offset
        self.selector_index += real_offset
        self.update_player_carried()
