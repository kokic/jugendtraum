from ursina import Entity, curve, Sequence, Func

from assets import AssetsManager

offset = (0, 0.2, 0)
half_duration = 1.5


class Dropping(Entity):

    def __init__(self, **kwargs):
        super().__init__(
            model=AssetsManager.get_model('dropping'),
            texture=AssetsManager.get_items_image('bow_standby'),
        )

        self.scale = 0.4

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.lifting_animate()
        self.sequence = Sequence(Func(self.lifting_animate), duration=half_duration * 2, loop=True)
        self.sequence.start()

    def lifting_animate(self):
        seq = self.animate_position(
            value=self.position + offset,
            duration=half_duration,
            curve=curve.in_out_quad
        )[0]

        seq.append(Func(lambda: self.animate_position(
            value=self.position - offset,
            duration=half_duration,
            curve=curve.in_out_quad,
        )))

        self.animate_rotation(
            value=self.rotation + (0, -180, 0),
            duration=half_duration * 2,
            curve=curve.linear
        )


class DroppingGroupBuilder:
    pass

