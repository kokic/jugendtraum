from enum import auto, Enum

from ursina import Vec3

from assets import Assets
from data.option import Option
from gui.component.ui_element import UIElement


class SlotEntityType(Enum):
    ITEM = auto(),
    BLOCK = auto(),

    def is_item(self):
        return self is SlotEntityType.ITEM

    def is_block(self):
        return self is SlotEntityType.BLOCK

    def get_scale(self) -> float:
        if self.is_item():
            return 0.035
        elif self.is_block():
            return 0.022

    def get_rotation(self) -> Vec3:
        if self is SlotEntityType.ITEM:
            return Vec3(0, 0, 0)
        elif self is SlotEntityType.BLOCK:
            return Vec3(-15, 45, 15)


class SlotEntity(UIElement):
    def __init__(self, ratio=1, **kwargs):
        super().__init__(
            use_ratio_scale=False,
            z=-1,
            texture=Assets.apple,
            model='dropping',
            scale=SlotEntityType.ITEM.get_scale() * Option.ui_scale / ratio
        )

        self.ratio = ratio
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

    def update_transform(self):
        self.scale = self.type.get_scale() * Option.ui_scale / self.ratio
        self.rotation = self.type.get_rotation()
