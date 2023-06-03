from block.block import Block


class Level:

    @staticmethod
    def set_block(identifier: str, position):
        if identifier in Block.blocks:
            Block.blocks[identifier].place(position)
        else:
            print(f"block {identifier} not exists!")


