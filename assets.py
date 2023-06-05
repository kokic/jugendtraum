import os

from PIL import Image
from ursina import Texture, color


class AssetsManager:
    @staticmethod
    def get_model(name):
        return f"models/{name}"

    @staticmethod
    def get_mob_path(name):
        return f"models/mob/{name}"

    @staticmethod
    def get_items_path(name):
        return f"images/items/{name}"

    @staticmethod
    def get_blocks_path(name):
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
        top_image = Image.open(AssetsManager.get_blocks_path(top))
        side_image = Image.open(AssetsManager.get_blocks_path(side))
        bottom_image = Image.open(AssetsManager.get_blocks_path(bottom))
        image = Image.open('images/empty_48x16.png')
        image.paste(top_image, (0, 0))
        image.paste(side_image, (16, 0))
        image.paste(bottom_image, (32, 0))
        return Texture(image)


# JSON
class Assets:
    # models
    dropping = AssetsManager.get_model('dropping')
    isotropic = AssetsManager.get_model('isotropic')
    block = AssetsManager.get_model('block')

    # item texture
    empty = Texture(Image.new('RGBA', (16, 16), color=(0, 0, 0, 0)))
    apple = AssetsManager.get_items_path('apple')
    apple_golden = AssetsManager.get_items_path('apple_golden')
    carrot = AssetsManager.get_items_path('carrot')

    ender_eye = AssetsManager.get_items_path('ender_eye.png')

    # block texture
    dirt = AssetsManager.get_blocks_path('isotropic/dirt')
    planks_oak = AssetsManager.get_blocks_path('isotropic/planks_oak')

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

    sandstone_normal = AssetsManager.block_texture_48x16(
        'sandstone_top.png',
        'sandstone_normal.png',
        'sandstone_bottom.png'
    )

    sandstone_smooth = AssetsManager.block_texture_48x16(
        'sandstone_top.png',
        'sandstone_smooth.png',
        'sandstone_bottom.png'
    )

    tnt = AssetsManager.block_texture_3('tnt')

    piston = AssetsManager.block_texture_3('piston')
    stick_piston = AssetsManager.block_texture_48x16(
        'piston_top_sticky.png',
        'piston_side.png',
        'piston_bottom.png'
    )

    endframe = AssetsManager.block_texture_48x16(
        'endframe_top.png',
        'endframe_side.png',
        'end_stone.png'
    )
    endframe_eye = AssetsManager.get_blocks_path('endframe_eye.png')

    enchanting_table = AssetsManager.block_texture_48x16(
        'enchanting_table_top.png',
        'enchanting_table_side.png',
        'enchanting_table_bottom.png'
    )

#
# isotropic = os.listdir(AssetsManager.get_blocks_image('isotropic'))
# for name in isotropic:
#     setattr(Assets, name, AssetsManager.get_blocks_image(f'isotropic/{name}'))
#

# image = Image.new('RGBA', (48, 16), color=(0, 0, 0, 0))
# image.save('block.png')
