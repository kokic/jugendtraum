from ursina import destroy, Button, color, scene, mouse, Entity

from assets import AssetsManager, Assets
from entity.carried import CarriedItem
from etale.client import client


class Block:
    blocks = {}

    @staticmethod
    def register_block(identifier, block):
        block.identifier = identifier
        Block.blocks[identifier] = block

    def __init__(self, model='block', texture=None, **kwargs):
        self.model = model
        self.texture = texture
        self.identifier = 'block'
        self.collider = 'box'

        self.slot_entity_model = model
        self.slot_entity_texture = texture

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_remove(self, level_block: Entity):
        destroy(level_block)

    def use_model(self, name):
        return self.model == AssetsManager.get_model(name)

    def update_model(self, name):
        self.model = name

    def is_hovered(self, level_block: Entity):
        return level_block.hovered

    def place(self, position):
        level_block = place_prototype_block(self.model, self.texture, position)
        level_block.collider = self.collider
        level_block.input = lambda key: self.input(level_block, key)
        return level_block

    def on_use(self, position):
        self.place(position + mouse.world_normal)

    def on_use_carried(self, level_block: Entity, carried: CarriedItem):
        pass

    def debug_on_hover_press(self, level_block: Entity, key):
        return

    def input(self, level_block: Entity, key):
        if client.player_operation_blocked:
            return

        if self.is_hovered(level_block):
            if key == 'left mouse down':
                self.on_remove(level_block)
            elif key == 'right mouse down':
                carried = client.player.carried
                identifier = carried.identifier
                if carried.entity_type.is_block() and identifier in Block.blocks:
                    Block.blocks[identifier].on_use(level_block.position)
                else:
                    self.on_use_carried(level_block, carried)

            self.debug_on_hover_press(level_block, key)


def place_prototype_block(model, texture, position):
    prototype_block = Button(model=model, texture=texture, position=position)
    prototype_block.parent = scene
    prototype_block.color = color.color(0, 0, 0.85)
    prototype_block.highlight_color = color.white
    return prototype_block


class IsotropicBlock(Block):
    def __init__(self, texture=Assets.dirt, **kwargs):
        super().__init__(model='isotropic', texture=texture)
        for key, value in kwargs.items():
            setattr(self, key, value)
