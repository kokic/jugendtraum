import math

from PIL import Image
from ursina import Texture, mouse, Vec3

from assets import Assets, AssetsManager
from data.option import Option
from gui.component.slot import SlotData
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

hotbar_slots_y = -0.133 * Option.ui_scale


class InventorySlotEntity(SlotEntity):

    def __init__(self, **kwargs):
        super().__init__(ratio=1.1)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_click(self):
        # copies inventory_slot data to mouse_selected
        if not self.is_slot_empty():
            from etale.client import client
            inv: InventoryUI = client.inventory_ui
            self.get_data().set_data_to(inv.mouse_selected)


class InventoryUI(UIElement):

    def __init__(self):
        super().__init__(
            texture=inventory_texture,
            scale=0.35 * Option.ui_scale
        )

        # self.z = -1
        self.items: list[SlotData] = []
        self.page_index = 0
        # self.pages = []

        # 27
        self.slots: list[InventorySlotEntity] = []
        self.slot_counter = 0
        self.mouse_selected = SlotEntity(ratio=1.1, always_on_top=True)
        self.hotbar_slots = []

        # from assets import Assets
        # self.slots.append(InventorySlotEntity(
        #     texture=Assets.carrot,
        #     x=slot_min_x + self.slot_index % 9 * slot_off_unit,
        #     y=slot_min_y - self.slot_index // 9 * slot_off_unit,
        #     ratio=1.1,
        # ))
        # self.slot_index += 1

        # import os
        # for name in os.listdir(AssetsManager.get_items_path('')):
        #     data = SlotData(
        #         model=Assets.dropping,
        #         texture=AssetsManager.get_items_path(name),
        #         entity_type=SlotEntityType.ITEM,
        #         identifier=name[:-4]
        #     )
        #     self.items.append(data)

        from item.item import Item
        for item in Item.items.values():
            data = SlotData(
                model=Assets.dropping,
                texture=item.texture,
                entity_type=SlotEntityType.ITEM,
                identifier=item.identifier,
            )
            self.items.append(data)

        #

        from block.block import Block
        for block in Block.blocks.values():
            data = SlotData(
                model=block.slot_entity_model,
                texture=block.slot_entity_texture,
                entity_type=block.slot_entity_type,
                identifier=block.identifier,
            )
            self.items.append(data)

        #
        #
        #

        # count = min(len(self.items), 27)
        for item in self.items:
            self.create_slot(item)

        # self.max_page_index = (len(self.items) - 1) // 27
        self.max_page_index = (self.slot_counter - 1) // 27

        for n in range(9):
            hotbar_slot = InventorySlotEntity(
                x=slot_min_x + n % 9 * slot_off_unit,
                y=hotbar_slots_y
            )
            hotbar_slot.index = n
            # don't copies
            hotbar_slot.input = None
            hotbar_slot.on_click = self.on_hotbar_slot_click(hotbar_slot)
            self.hotbar_slots.append(hotbar_slot)

        # self.debug_set_slot()

        # wait for all children
        self.disable()

    def debug_set_slot(self):
        SlotData(
            texture=Assets.piston,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='piston',
        ).set_data_to(self.hotbar_slots[0])

        SlotData(
            texture=AssetsManager.get_items_path('iron_pickaxe'),
            entity_type=SlotEntityType.ITEM
        ).set_data_to(self.hotbar_slots[1])

        SlotData(
            texture=Assets.tnt,
            model=Assets.block,
            entity_type=SlotEntityType.BLOCK,
            identifier='tnt',
        ).set_data_to(self.hotbar_slots[2])

        SlotData(
            model=Assets.block,
            texture=Assets.sandstone_carved,
            entity_type=SlotEntityType.BLOCK,
            identifier='sandstone_carved',
        ).set_data_to(self.hotbar_slots[3])

    def on_hotbar_slot_click(self, hotbar_slot: InventorySlotEntity):
        def generator():
            from etale.client import client

            # case1. put mouse_selected item to hotbar_slot
            # case2. take hotbar_slot item to mouse_selected
            # case3. exchange

            hotbar_data = hotbar_slot.get_data()
            mouse_data = self.mouse_selected.get_data()

            hotbar_data.set_data_to(self.mouse_selected)
            mouse_data.set_data_to(hotbar_slot)

            client.hotbar_ui.set_slot(hotbar_slot.index, mouse_data)

        return generator

    def disable(self):
        mouse.locked = True

        from data.shared import Shared
        from etale.client import client
        if Shared.carried_bind_camera:
            client.player.cursor.enabled = True
            client.player_operation_blocked = False
        else:
            client.player.enable()

        self.mouse_selected.disable()

        for child in self.hotbar_slots:
            child.disable()

        for n in range(27):
            index = self.page_index * 27 + n
            if index < self.slot_counter:
                self.slots[index].disable()

        super().disable()

    def enable(self):
        mouse.locked = False

        from data.shared import Shared
        from etale.client import client
        if Shared.carried_bind_camera:
            # client.player.disable()
            client.player.cursor.enabled = False
            client.player_operation_blocked = True
        else:
            client.player.disable()

        self.mouse_selected.enable()

        for child in self.hotbar_slots:
            child.enable()

        for n in range(27):
            index = self.page_index * 27 + n
            if index < self.slot_counter:
                self.slots[index].enable()

        super().enable()

    def set_slot(self, index, data: SlotData):
        data.set_data_to(self.hotbar_slots[index])

        if index < 9:
            from etale.client import client
            client.hotbar_ui.set_slot(index, data)

    def create_slot(self, item: SlotData):
        # if self.slot_index >= 27:
        #     return

        offset = self.slot_counter % 27

        # texture = item.slot_entity_texture if hasattr(item, 'slot_entity_texture') else item.texture
        # model = item.slot_entity_model if hasattr(item, 'slot_entity_model') else item.model

        self.slots.append(InventorySlotEntity(
            texture=item.texture,
            model=item.model,
            x=slot_min_x + offset % 9 * slot_off_unit,
            y=slot_min_y - offset // 9 * slot_off_unit,
            entity_type=item.entity_type,
            identifier=item.identifier,
            enabled=False
        ))
        self.slot_counter += 1

    def prev_page_items(self):
        if self.page_index == 0:
            return

        for n in range(27):
            index = self.page_index * 27 + n
            if index < self.slot_counter:
                self.slots[index].disable()
            self.slots[(self.page_index - 1) * 27 + n].enable()
            # index = self.page_index * 27 + n
            # self.items[index].set_data_to(self.slots[n])

        self.page_index -= 1

    def next_page_items(self):
        if self.page_index == self.max_page_index:
            return

        for n in range(27):
            self.slots[self.page_index * 27 + n].disable()
            index = (self.page_index + 1) * 27 + n
            if index < self.slot_counter:
                self.slots[index].enable()
            # item = self.items[index] if index < len(self.items) else SlotData.empty
            # item.set_data_to(self.slots[n])

        self.page_index += 1

    def input(self, key):
        # throw mouse_selected item if right mouse down
        if key == 'right mouse down' and not self.mouse_selected.is_slot_empty():
            return self.mouse_selected.set_slot_empty()

        if key == 'up arrow':
            return self.prev_page_items()

        if key == 'down arrow':
            return self.next_page_items()
