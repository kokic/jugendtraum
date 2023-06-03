from ursina import curve, Func, Sequence, Entity

from assets import Assets
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
            texture=Assets.enchanting_table,
        )

        # self.collider = 'mesh'
        # self.book = EntityBlock(
        #     fetch_asset('enchanting-table-book'),
        #     fetch_asset('enchanting_table_book.png')
        # )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def place(self, position):
        level_block = super().place(position)
        level_block.book = EntityBlock(
            fetch_asset('enchanting-table-book'),
            fetch_asset('enchanting_table_book.png'),
            parent=level_block
        )

        func = Func(lambda: EnchantingTable.book_animate_aux(level_block))
        level_block.sequence = Sequence(func, duration=half_duration * 2, loop=True)
        # level_block.can_play_animate = True
        EnchantingTable.book_animate(level_block)

        return level_block

    @staticmethod
    def book_animate(level_block: Entity):
        EnchantingTable.book_animate_aux(level_block)
        level_block.sequence.start()

    @staticmethod
    def book_animate_aux(level_block: Entity):
        # if not self.can_play_animate:
        #     return

        pos = level_block.book.position + offset
        seq = level_block.book.animate_position(
            value=pos,
            duration=half_duration,
            curve=curve.linear,
        )[0]

        seq.append(Func(lambda: level_block.book.animate_position(
            value=pos - offset,
            duration=half_duration,
            curve=curve.linear
        )))

        level_block.book.animate_rotation(
            value=level_block.book.rotation + (0, 180, 0),
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
