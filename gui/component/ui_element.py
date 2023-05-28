from ursina import Entity, camera


class UIElement(Entity):

    def __init__(self, use_ratio_scale=True, **kwargs):
        super().__init__(model='quad', parent=camera.ui)

        for key, value in kwargs.items():
            setattr(self, key, value)

        if use_ratio_scale:
            self.aspect_ratio = self.texture.height / self.texture.width
            self.scale_y = self.scale_x * self.aspect_ratio

