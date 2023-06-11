from ursina import mouse

from assets import AssetsManager, Assets
from block.block import Block
from etale.face import get_face_from_normal
from gui.component.slot import SlotEntityType


def fetch_asset(name):
    return f"models/torch/{name}"


class Torch(Block):

    def __init__(self, texture=AssetsManager.get_blocks_path('torch_on')):
        super().__init__(
            model=fetch_asset('torch'),
            texture=texture,
            slot_entity_type=SlotEntityType.ITEM,
            slot_entity_model=Assets.dropping,
        )

    def place(self, position):
        face = get_face_from_normal(mouse.world_normal)

        if not face.bottom():

            if face.top():
                level_block = super().place(position)
                return level_block

            level_block = super().place(position)
            level_block.model = fetch_asset('torch_side')
            level_block.collider = 'mesh'

            if face.back():
                level_block.rotation_y = 180

            if face.left():
                level_block.rotation_y = 90

            if face.right():
                level_block.rotation_y = -90

            return level_block
