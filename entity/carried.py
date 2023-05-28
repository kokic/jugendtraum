from ursina import Entity, Vec3, camera

from assets import Assets
from data.option import Option
from gui.hud_screen import SlotEntityType, HotbarSlotEntity

# player hand-carried model:
# - empty (hand model)
# - item (dropping model)
# - block (block model)


origin = (0, -0.5, 0)

item_position = Vec3(0.7, -0.35, 1)
item_rotation = Vec3(0, 75, -30)
#
# item_use_position = Vec3(0.85, -0.55, 1)
# item_use_rotation = Vec3(0, 45, 0)

block_position = Vec3(0.85, -0.55, 1)
block_rotation = Vec3(0, 45, 0)


#
# block_use_position = Vec3(0.85, -0.55, 1)
# block_use_rotation = Vec3(0, 45, 0)
#

class UseAnimation:
    pass


class CarriedItem(Entity):

    def __init__(self, model=Assets.dropping, texture=Assets.apple, **kwargs):
        super().__init__(
            model=model,
            texture=texture,
            position=item_position,
            rotation=item_rotation,
            origin=origin,
            scale=0.5,
            parent=camera
        )

        self.entity_type = SlotEntityType.ITEM
        self.identifier = 'block'

        for key, value in kwargs.items():
            setattr(self, key, value)


    @property
    def entity_type(self):
        return self.type

    @entity_type.setter
    def entity_type(self, entity_type: SlotEntityType):
        self.type = entity_type
        self.update_transform()

    def set_entity(self, entity: HotbarSlotEntity):
        self.model = entity.model.name
        self.texture = entity.texture
        self.entity_type = entity.entity_type
        self.identifier = entity.identifier

    def update_transform(self):

        if self.entity_type is SlotEntityType.ITEM:
            self.position = item_position
            self.rotation = item_rotation

        elif self.entity_type is SlotEntityType.BLOCK:
            self.position = block_position
            self.rotation = block_rotation

        # print(self.entity_type.name)

    def on_left_mouse(self):
        pass

    def on_right_mouse(self):
        pass

    def input(self, key):
        if key == 'left mouse down':
            self.on_left_mouse()

        if key == 'left mouse down':
            self.on_right_mouse()
