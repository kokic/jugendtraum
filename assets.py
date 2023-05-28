from PIL import Image
from ursina import Texture, color


class AssetsManager:
    @staticmethod
    def get_model(name):
        return f"models/{name}"

    @staticmethod
    def get_items_image(name):
        return f"images/items/{name}"

    @staticmethod
    def get_blocks_image(name):
        return f"images/blocks/{name}"

    @staticmethod
    def block_texture_3(name) -> Texture:
        return AssetsManager.block_texture_48x16(
            f"{name}_top.png",
            f"{name}_side.png",
            f"{name}_bottom.png"
        )

    @staticmethod
    def block_texture_48x16(top, side, bottom) -> Texture:
        top_image = Image.open(AssetsManager.get_blocks_image(top))
        side_image = Image.open(AssetsManager.get_blocks_image(side))
        bottom_image = Image.open(AssetsManager.get_blocks_image(bottom))
        image = Image.open('images/block_48x16.png')
        image.paste(top_image, (0, 0))
        image.paste(side_image, (16, 0))
        image.paste(bottom_image, (32, 0))
        return Texture(image)


class Assets:
    # models
    block = AssetsManager.get_model('block')
    dropping = AssetsManager.get_model('dropping')

    # item texture
    apple = AssetsManager.get_items_image('apple')

    # block texture
    grass = AssetsManager.block_texture_48x16(
        'grass_carried.png',
        'grass_side_carried.png',
        'dirt.png'
    )

    sandstone_carved = AssetsManager.block_texture_48x16(
        'sandstone_top.png',
        'sandstone_carved.png',
        'sandstone_bottom.png'
    )

    tnt = AssetsManager.block_texture_3('tnt')

    piston = AssetsManager.block_texture_3('piston')
    stick_piston = AssetsManager.block_texture_48x16(
        'piston_top_sticky.png',
        'piston_side.png',
        'piston_bottom.png'
    )

# image = Image.new('RGBA', (48, 16), color=(0, 0, 0, 0))
# image.save('block.png')
