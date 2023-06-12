from ursina import destroy, Button, color, scene, mouse, Entity

from assets import AssetsManager, Assets
from entity.carried import CarriedItem
from etale.client import client
from gui.component.slot import SlotEntityType
from item.item import Item


class Block:
    blocks = {}

    @staticmethod
    def register_block(identifier, block):
        block.identifier = identifier
        Block.blocks[identifier] = block

    def __init__(self, model=Assets.block, texture=None, **kwargs):
        self.model = model
        self.texture = texture
        self.identifier = 'block'
        self.collider = 'box'

        self.slot_entity_model = model
        self.slot_entity_texture = texture
        self.slot_entity_type = SlotEntityType.BLOCK

        self.sound_name_on_destroy = 'dig-stone1'

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_remove(self, level_block: Entity):
        destroy(level_block)

    def use_model(self, name):
        return self.model == AssetsManager.get_model_path(name)

    def update_model(self, name):
        self.model = name

    def is_hovered(self, level_block: Entity):
        return level_block.hovered

    def place(self, position):
        level_block = place_prototype_block(self.model, self.texture, position)
        level_block.block = self
        level_block.collider = self.collider
        level_block.input = lambda key: self.input(level_block, key)
        return level_block

    def on_use(self, level_block: Entity, position):
        self.place(position + mouse.world_normal)

    def debug_on_hover_press(self, level_block: Entity, key):
        return

    def on_right_mouse_down(self, level_block: Entity, carried: CarriedItem) -> bool:
        return False

    # carried empty and target has an item ...
    def on_take_out(self, level_block: Entity):
        pass

    def input(self, level_block: Entity, key):
        if client.player_operation_blocked:
            return

        if self.is_hovered(level_block):
            if key == 'left mouse down':
                self.on_remove(level_block)
                AssetsManager.get_sound(self.sound_name_on_destroy).play()

            elif key == 'right mouse down':

                carried = client.player.carried
                identifier = carried.identifier

                if self.on_right_mouse_down(level_block, carried):
                    return

                if identifier in Block.blocks:
                    block: Block = Block.blocks[identifier]
                    block.on_use(level_block, level_block.position)
                    AssetsManager.get_sound(block.sound_name_on_destroy).play()

                elif identifier in Item.items:
                    item: Item = Item.items[identifier]
                    item.use_on(carried, self, level_block)

                elif carried.entity_type.is_empty():
                    self.on_take_out(level_block)

            self.debug_on_hover_press(level_block, key)


def place_prototype_block(model, texture, position):
    prototype_block = Button(model=model, texture=texture, position=position)
    prototype_block.parent = scene
    prototype_block.color = color.color(0, 0, 0.85)
    prototype_block.highlight_color = color.white
    return prototype_block


class IsotropicBlock(Block):
    def __init__(self, texture=Assets.dirt, **kwargs):
        super().__init__(model=Assets.isotropic, texture=texture)
        for key, value in kwargs.items():
            setattr(self, key, value)
