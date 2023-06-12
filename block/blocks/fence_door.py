from ursina import Entity

from assets import Assets
from block.block import Block
from entity.carried import CarriedItem


def fetch_asset(name):
    return f"models/fence_door/{name}"


class FenceDoor(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('fence-door'),
            texture=Assets.planks_oak,
        )

        self.collider = 'mesh'

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_right_mouse_down(self, level_block: Entity, carried: CarriedItem) -> bool:
        if level_block.model.name == fetch_asset('fence-door'):
            level_block.model = fetch_asset('fence-door-open')

        elif level_block.model.name == fetch_asset('fence-door-open'):
            level_block.model = fetch_asset('fence-door')

        level_block.collider = 'mesh'

        # prevent default
        return True

    # def debug_on_hover_press(self, level_block: Entity, key):
    #     if key == 'm':
    #         if level_block.model.name == fetch_asset('fence-door'):
    #             level_block.model = fetch_asset('fence-door-open')
    #
    #         elif level_block.model.name == fetch_asset('fence-door-open'):
    #             level_block.model = fetch_asset('fence-door')
    #
    #         # model update
    #         level_block.collider = 'mesh'

