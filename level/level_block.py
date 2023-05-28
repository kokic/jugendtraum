from ursina import Button, scene, color


# TODO: replace Block with this

class LevelBlock(Button):
    def __init__(self, **kwargs):
        super().__init__(
            parent=scene,
            color=color.color(0, 0, 0.85),
            highlight_color=color.white
        )

        for key, value in kwargs.items():
            setattr(self, key, value)
