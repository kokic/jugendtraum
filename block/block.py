from ursina import destroy, Button, color, scene, mouse

from assets import AssetsManager
from client import client, get_face_from_normal


class Block(Button):
    def __init__(self, model='block', texture=None, position=(0, 0, 0), **kwargs):
        super().__init__(
            model=model,
            texture=texture,
            position=position,
            parent=scene,
            color=color.color(0, 0, 0.85),
            highlight_color=color.white,
        )

        self.identifier = 'block'
        self.model_name = model

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_remove(self):
        destroy(self)

    def use_model(self, name):
        return self.model_name == AssetsManager.get_model(name)

    def update_model(self, name):
        self.model = self.model_name = name

    def is_hovered(self):
        return self.hovered

    def place(self, position):
        carried = client.player.carried
        if carried.entity_type.is_block():

            if carried.identifier == 'piston':
                from block.piston import PistonBlock
                block = PistonBlock(position=position)
                block.face = get_face_from_normal(mouse.world_normal)
                return block

            return Block(
                model=carried.model.name,
                texture=carried.texture,
                position=position
            )

    def on_use(self):
        self.place(self.position + mouse.world_normal)

    def debug_on_hover_press(self, key):
        return

    def input(self, key):
        if self.is_hovered():
            if key == 'left mouse down':
                self.on_remove()
            elif key == 'right mouse down':
                self.on_use()

            self.debug_on_hover_press(key)
