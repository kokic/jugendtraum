from ursina import Entity

from block.block import Block


def fetch_asset(name):
    return f"models/fence_door/{name}"


class FenceDoor(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('fence-door'),
            texture=fetch_asset('planks_oak.png'),
        )

        self.collider = 'box'

        for key, value in kwargs.items():
            setattr(self, key, value)

    def place(self, position):
        return FenceDoor(position=position)

    def toggle(self):
        if self.model == fetch_asset('fence-door'):
            self.update_model(fetch_asset('fence-door-open'))
            self.collider = 'mesh'

        elif self.model == fetch_asset('fence-door-open'):
            self.update_model(fetch_asset('fence-door'))
            self.collider = 'box'

    def debug_on_hover_press(self, level_block: Entity, key):
        if key == 'm':
            self.toggle()
