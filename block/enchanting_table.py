import math
import random

from ursina import curve, Func, Sequence

from block.block import Block
from entity.entity import EntityBlock


def fetch_asset(name):
    return f"models/enchanting_table/{name}"


offset = (0, 0.2, 0)
half_duration = 4


class EnchantingTable(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('enchanting-table'),
            texture=fetch_asset('enchanting_table.png'),
        )

        # self.collider = 'mesh'
        self.book = EntityBlock(
            fetch_asset('enchanting-table-book'),
            fetch_asset('enchanting_table_book.png')
        )
        self.book.parent = self

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.sequence = Sequence(Func(self.book_animate_aux), duration=half_duration * 2, loop=True)

        self.period_value = 0

        self.can_play_animate = True
        self.book_animate()

    # def place(self, position):
    #     return EnchantingTable(position=position)

    def book_animate(self):
        self.book_animate_aux()
        self.sequence.start()

    def book_animate_aux(self):
        if not self.can_play_animate:
            return

        pos = self.book.position + offset
        seq = self.book.animate_position(
            value=pos,
            duration=half_duration,
            curve=curve.linear,
        )[0]

        seq.append(Func(lambda: self.book.animate_position(
            value=pos - offset,
            duration=half_duration,
            curve=curve.linear
        )))

        self.book.animate_rotation(
            value=self.book.rotation + (0, 180, 0),
            duration=half_duration * 2,
            curve=curve.linear
        )

        # scale = self.book.animate_scale(
        #     value=1.6,
        #     duration=half_duration,
        # )
        # scale.append(Func(lambda: self.book.animate_scale(
        #     value=0.8,
        #     duration=half_duration
        # )))
