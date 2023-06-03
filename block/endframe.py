from ursina import Entity

from assets import AssetsManager, Assets
from block.block import Block
from entity.carried import CarriedItem
from entity.entity import EntityBlock


def fetch_asset(name):
    return f"models/endframe/{name}"


class EndFrame(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('endframe'),
            texture=Assets.endframe,
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def place(self, position):
        level_block = super().place(position)
        level_block.eye = EntityBlock(
            fetch_asset('endframe-eye'),
            AssetsManager.get_blocks_path('endframe_eye.png'),
            parent=level_block,
            enabled=False
        )

        return level_block

    def on_use_carried(self, level_block: Entity, carried: CarriedItem):
        eye = level_block.eye
        if carried.identifier == 'ender_eye' and not eye.enabled:
            eye.enable()

        elif carried.identifier == 'empty' and eye.enabled:
            eye.disable()


    # def debug_on_hover_press(self, level_block: Entity, key):
    #     if key == 'p':
    #         if level_block.eye.enabled:
    #             level_block.eye.disable()
    #         else:
    #             level_block.eye.enable()
