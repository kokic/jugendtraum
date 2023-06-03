from ursina import Entity, destroy

from assets import AssetsManager


# an entity with block behavior (as block model)
class EntityBlock(Entity):
    def __init__(self, model='cube', texture=None, position=(0, 0, 0), **kwargs):
        super().__init__(
            model=model,
            texture=texture,
            position=position,
        )

        self.model_name = model

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_remove(self):
        destroy(self)

    def use_model(self, name):
        return self.model_name == AssetsManager.get_model(name)

    def update_model(self, name):
        self.model = self.model_name = name


class EntityFactory:

    @staticmethod
    def entity_extra(model, texture, position):
        e = Entity(model=model, texture=texture, position=position)
        e.model_name = model
        return e

    @staticmethod
    def entity(model, texture, position):
        return EntityFactory.entity_extra(f"models/{model}", texture, position)
