from ursina import application, load_model

from block.block import Block


def fetch_asset(name):
    return f"models/endframe/{name}"


class EndFrame(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('endframe'),
            texture=fetch_asset('endframe.png'),
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def place(self, position):
        return EndFrame(position=position)

    def debug_on_hover_press(self, key):
        if key == 'p':
            if self.model_name == fetch_asset("endframe"):
                self.update_model(fetch_asset("endframe-eye"))

            elif self.model_name == fetch_asset("endframe-eye"):
                self.update_model(fetch_asset("endframe"))

