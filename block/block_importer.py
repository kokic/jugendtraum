

def init_blocks():

    # isotropic

    import os
    from assets import Assets
    from assets import AssetsManager

    from block.block import IsotropicBlock, Block
    isotropic = os.listdir(AssetsManager.get_blocks_path('isotropic'))
    for filename in isotropic:
        texture = AssetsManager.get_blocks_path(f'isotropic/{filename}')
        # identifier.png
        identifier = filename[:-4]
        Block.register_block(identifier, IsotropicBlock(texture))

    # block

    Block.register_block('grass', Block(model=Assets.block, texture=Assets.grass))
    Block.register_block('tnt', Block(model=Assets.block, texture=Assets.tnt))
    Block.register_block('sandstone_carved', Block(model=Assets.block, texture=Assets.sandstone_carved))
    Block.register_block('sandstone_normal', Block(model=Assets.block, texture=Assets.sandstone_normal))
    Block.register_block('sandstone_smooth', Block(model=Assets.block, texture=Assets.sandstone_smooth))

    from block.piston import PistonBlock
    from block.piston import StickPistonBlock
    Block.register_block('piston', PistonBlock())
    Block.register_block('stick_piston', StickPistonBlock())

    from block.endframe import EndFrame
    Block.register_block('endframe', EndFrame())

    from block.enchanting_table import EnchantingTable
    Block.register_block('enchanting_table', EnchantingTable())

    from block.fence_door import FenceDoor
    Block.register_block('fence_door', FenceDoor())




