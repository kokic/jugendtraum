from ursina import Entity, camera


class UIElement(Entity):

    def __init__(self, **kwargs):
        super().__init__(model='quad', parent=camera.ui)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.aspect_ratio = self.texture.width / self.texture.height
        self.scale_x = self.scale_y * self.aspect_ratio
