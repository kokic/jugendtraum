from ursina import Entity, Vec3, camera

from assets import Assets
from data.shared import Shared
from gui.hud import SlotEntityType

# player hand-carried model:
# - empty (hand model)
# - item (dropping model)
# - block (block model)


origin = (0, -0.5, 0)

# TODO: smooth x

# item_use_position = Vec3(0.85, -0.55, 1)
# item_use_rotation = Vec3(0, 45, 0)


if Shared.carried_bind_camera:
    # in camera
    item_position = Vec3(0.7, -0.35, 1)
    item_rotation = Vec3(0, 75, -30)
    #
    block_position = Vec3(0.85, -0.55, 1)
    block_rotation = Vec3(0, 45, 0)
else:
    # in camera.ui
    item_position = Vec3(0.7, -0.35, 1)
    item_rotation = Vec3(5, 55, -30)
    #
    block_position = Vec3(0.7, -0.5, 1)
    block_rotation = Vec3(-8, -60, -16)


#
# block_use_position = Vec3(0.85, -0.55, 1)
# block_use_rotation = Vec3(0, 45, 0)
#

class UseAnimation:
    pass


class CarriedItem(Entity):

    def __init__(self, model=Assets.dropping, texture=Assets.empty, **kwargs):
        super().__init__(
            model=model,
            texture=texture,
            position=item_position,
            rotation=item_rotation,
            origin=origin,
            # scale=0.5,
            scale=0.4,
            always_on_top=False,
            parent=camera if Shared.carried_bind_camera else camera.ui
        )

        self.entity_type = SlotEntityType.EMPTY
        self.identifier = 'empty'

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def entity_type(self):
        return self.type

    @entity_type.setter
    def entity_type(self, entity_type: SlotEntityType):
        self.type = entity_type
        self.update_transform()

    def update_transform(self):
        if self.entity_type is SlotEntityType.EMPTY:
            # here handle player hand model
            pass

        elif self.entity_type is SlotEntityType.ITEM:
            self.rotation = item_rotation
            self.x = item_position.x
            # self.position = item_position

        elif self.entity_type is SlotEntityType.BLOCK:
            self.rotation = block_rotation
            self.x = block_position.x
            # self.position = block_position

    def on_left_mouse(self):
        pass

    def on_right_mouse(self):
        pass

    def input(self, key):
        if key == 'left mouse down':
            self.on_left_mouse()

        if key == 'left mouse down':
            self.on_right_mouse()

        if key == 'x':
            self.rotation_x -= 10
        if key == 'y':
            self.rotation_y -= 10
        if key == 'z':
            self.rotation_z -= 10

        if key == 'p':
            print((self.rotation_x % 360, self.rotation_y % 360, self.rotation_z % 360))

    @staticmethod
    def get_base_position(entity_type: SlotEntityType):
        if entity_type is SlotEntityType.BLOCK:
            return block_position
        return item_position
