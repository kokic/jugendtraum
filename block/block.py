from ursina import destroy, Button, color, scene, mouse, Entity

from assets import AssetsManager, Assets
from client import client, get_face_from_normal


class Block:
    blocks = {}

    @staticmethod
    def register_block(identifier, block):
        block.identifier = identifier
        Block.blocks[identifier] = block

    @staticmethod
    def init_blocks():

        Block.register_block('grass', Block(model=Assets.block, texture=Assets.grass))
        Block.register_block('tnt', Block(model=Assets.block, texture=Assets.tnt))
        Block.register_block('sandstone_carved', Block(model=Assets.block, texture=Assets.sandstone_carved))

        # from block.piston import PistonBlock
        # Block.register_block('piston', PistonBlock())
        #
        # from block.piston import StickPistonBlock
        # Block.register_block('stick_piston', StickPistonBlock())

    def __init__(self, model='block', texture=None, **kwargs):
        # super().__init__(
        #     model=model,
        #     texture=texture,
        #     parent=scene,
        #     color=color.color(0, 0, 0.85),
        #     highlight_color=color.white,
        # )

        self.model = model
        self.texture = texture
        self.identifier = 'block'

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
        # carried = client.player.carried
        # if carried.entity_type.is_block():
        #
        #     if carried.identifier in Block.blocks:
        #         return Block.blocks[carried.identifier].place(position)
        #
        level_block = Button(model=self.model, texture=self.texture, position=position)
        level_block.parent = scene
        level_block.color = color.color(0, 0, 0.85)
        level_block.highlight_color = color.white
        level_block.input = lambda key: self.input(level_block, key)

        return level_block

    def on_use(self, position):
        self.place(position + mouse.world_normal)

    def debug_on_hover_press(self, level_block: Entity, key):
        return

    def input(self, level_block: Entity, key):
        if self.is_hovered(level_block):
            if key == 'left mouse down':
                self.on_remove(level_block)
            elif key == 'right mouse down':
                carried = client.player.carried
                identifier = carried.identifier
                if carried.entity_type.is_block() and identifier in Block.blocks:
                    Block.blocks[identifier].on_use(level_block.position)

            self.debug_on_hover_press(level_block, key)


class Level:

    @staticmethod
    def set_block(identifier: str, position):
        if identifier in Block.blocks:
            block = Block.blocks[identifier]
            block.place(position)
        # not exists
