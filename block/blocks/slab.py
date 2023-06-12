from ursina import Entity, destroy, mouse, Vec3

from assets import Assets
from block.block import Block
from entity.carried import CarriedItem
from etale.face import get_face_from_normal
from level.level import Level


class Slab(Block):

    def __init__(self, texture):
        super().__init__(model=Assets.slab, texture=texture)

    # def place(self, position):

    def on_right_mouse_down(self, level_block: Entity, carried: CarriedItem) -> bool:
        if get_face_from_normal(mouse.world_normal).top() \
                and level_block.model.name == Assets.slab \
                and carried.model.name == Assets.slab \
                and level_block.block.identifier == carried.identifier:

            Level.set_block(carried.identifier, level_block.position + Vec3(0, 0.5, 0))
            # planks_identifier = carried.identifier[:-5]
            # Level.set_block(planks_identifier, level_block.position)
            # destroy(level_block)

            return True

        return False
