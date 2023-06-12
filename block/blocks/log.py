from ursina import mouse

from assets import Assets
from block.block import Block
from etale.face import get_face_from_normal


class Log(Block):

    def __init__(self, texture):
        super().__init__(model=Assets.log, texture=texture)

    def place(self, position):
        face = get_face_from_normal(mouse.world_normal)
        level_block = super().place(position)

        if face.front() or face.back():
            level_block.rotation_x = 90

        if face.left() or face.right():
            level_block.rotation_z = 90


