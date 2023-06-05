from enum import auto, Enum

from ursina import Vec3, color

from assets import Assets
from data.option import Option
from gui.component.ui_element import UIElement


class SlotEntityType(Enum):
    EMPTY = auto(),
    ITEM = auto(),
    BLOCK = auto(),

    def is_empty(self):
        return self is SlotEntityType.EMPTY

    def is_item(self):
        return self is SlotEntityType.ITEM

    def is_block(self):
        return self is SlotEntityType.BLOCK

    def get_scale(self) -> Vec3 | float:
        if self.is_item():
            return 0.035
        elif self.is_block():
            return 0.022

        return 0.035

    def get_rotation(self) -> Vec3 | float:
        if self is SlotEntityType.ITEM:
            return 0
        elif self is SlotEntityType.BLOCK:
            return Vec3(-15, 45, 15)

        return 0


class SlotData:

    empty = None

    def __init__(self,
                 model=Assets.dropping,
                 texture=Assets.empty,
                 entity_type=SlotEntityType.EMPTY,
                 identifier='empty'):
        self.model = model
        self.texture = texture
        self.entity_type = entity_type
        self.identifier = identifier

    def set_data_to(self, target):
        target.model = self.model
        target.texture = self.texture
        target.entity_type = self.entity_type
        target.identifier = self.identifier


SlotData.empty = SlotData()


class SlotEntity(UIElement):
    def __init__(self, ratio=1, **kwargs):
        super().__init__(
            collider='box',
            use_ratio_scale=False,
            z=-1,
            texture=Assets.empty,
            color=color.color(0, 0, 0.9),
            model='dropping',
            scale=SlotEntityType.ITEM.get_scale() * Option.ui_scale / ratio
        )

        self.ratio = ratio
        self.entity_type = SlotEntityType.EMPTY
        self.identifier = 'empty'

        for key, value in kwargs.items():
            setattr(self, key, value)

    def is_slot_empty(self):
        return self.entity_type == SlotEntityType.EMPTY \
            and self.texture == Assets.empty \
            and self.identifier == 'empty'

    def set_slot_empty(self):
        self.entity_type = SlotEntityType.EMPTY
        self.texture = Assets.empty
        self.identifier = 'empty'

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

    def get_data(self) -> SlotData:
        model = self.model if isinstance(self.model, str) else getattr(self.model, 'name')
        return SlotData(model, self.texture, self.entity_type, self.identifier)

    # @staticmethod
    # def set_data_from(target_slot, source_slot):
    #     target_slot.model = source_slot.model.name
    #     target_slot.texture = source_slot.texture
    #     target_slot.entity_type = source_slot.entity_type
    #     target_slot.identifier = source_slot.identifier

    # target_slot.alpha = 0 if target_slot.alpha is None else 1
