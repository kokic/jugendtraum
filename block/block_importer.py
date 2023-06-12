

def init_blocks():

    # import os
    # from assets import AssetsManager
    # isotropic = os.listdir(AssetsManager.get_blocks_path('isotropic'))
    # for filename in isotropic:
    #     texture = AssetsManager.get_blocks_path(f'isotropic/{filename}')
    #     # identifier.png
    #     identifier = filename[:-4]
    #     Block.register_block(identifier, IsotropicBlock(AssetsManager.get_blocks_path(f'isotropic/{filename}')))

    # isotropic

    from assets import Assets
    from block.block import IsotropicBlock, Block

    Block.register_block('bedrock', IsotropicBlock(Assets.bedrock))
    Block.register_block('brick', IsotropicBlock(Assets.brick))
    Block.register_block('coal_ore', IsotropicBlock(Assets.coal_ore))
    Block.register_block('cobblestone', IsotropicBlock(Assets.cobblestone))
    Block.register_block('cobblestone_mossy', IsotropicBlock(Assets.cobblestone_mossy))
    Block.register_block('command_block', IsotropicBlock(Assets.command_block))

    # until shaders
    # Block.register_block('concrete_black', IsotropicBlock(Assets.concrete_black))
    # Block.register_block('concrete_blue', IsotropicBlock(Assets.concrete_blue))
    # Block.register_block('concrete_brown', IsotropicBlock(Assets.concrete_brown))
    # Block.register_block('concrete_cyan', IsotropicBlock(Assets.concrete_cyan))
    # Block.register_block('concrete_gray', IsotropicBlock(Assets.concrete_gray))
    # Block.register_block('concrete_green', IsotropicBlock(Assets.concrete_green))
    # Block.register_block('concrete_light_blue', IsotropicBlock(Assets.concrete_light_blue))
    # Block.register_block('concrete_lime', IsotropicBlock(Assets.concrete_lime))
    # Block.register_block('concrete_magenta', IsotropicBlock(Assets.concrete_magenta))
    # Block.register_block('concrete_orange', IsotropicBlock(Assets.concrete_orange))
    # Block.register_block('concrete_pink', IsotropicBlock(Assets.concrete_pink))
    # Block.register_block('concrete_purple', IsotropicBlock(Assets.concrete_purple))
    # Block.register_block('concrete_red', IsotropicBlock(Assets.concrete_red))
    # Block.register_block('concrete_silver', IsotropicBlock(Assets.concrete_silver))
    # Block.register_block('concrete_white', IsotropicBlock(Assets.concrete_white))
    # Block.register_block('concrete_yellow', IsotropicBlock(Assets.concrete_yellow))

    Block.register_block('diamond_block', IsotropicBlock(Assets.diamond_block))
    Block.register_block('diamond_ore', IsotropicBlock(Assets.diamond_ore))
    Block.register_block('dirt', IsotropicBlock(Assets.dirt))
    Block.register_block('emerald_block', IsotropicBlock(Assets.emerald_block))

    Block.register_block('end_stone', IsotropicBlock(Assets.end_stone))
    Block.register_block('glowing_obsidian', IsotropicBlock(Assets.glowing_obsidian))
    Block.register_block('glowstone', IsotropicBlock(Assets.glowstone))
    Block.register_block('gold_block', IsotropicBlock(Assets.gold_block))
    Block.register_block('gold_ore', IsotropicBlock(Assets.gold_ore))
    Block.register_block('gravel', IsotropicBlock(Assets.gravel))
    Block.register_block('iron_block', IsotropicBlock(Assets.iron_block))
    Block.register_block('iron_ore', IsotropicBlock(Assets.iron_ore))
    Block.register_block('lapis_ore', IsotropicBlock(Assets.lapis_ore))
    Block.register_block('mob_spawner', IsotropicBlock(Assets.mob_spawner))
    Block.register_block('nether_brick', IsotropicBlock(Assets.nether_brick))

    Block.register_block('planks_acacia', IsotropicBlock(Assets.planks_acacia))
    Block.register_block('planks_big_oak', IsotropicBlock(Assets.planks_big_oak))
    Block.register_block('planks_birch', IsotropicBlock(Assets.planks_birch))
    Block.register_block('planks_jungle', IsotropicBlock(Assets.planks_jungle))
    Block.register_block('planks_oak', IsotropicBlock(Assets.planks_oak))
    Block.register_block('planks_spruce', IsotropicBlock(Assets.planks_spruce))

    from block.blocks.slab import Slab
    Block.register_block('planks_birch_slab', Slab(Assets.planks_birch))
    Block.register_block('planks_oak_slab', Slab(Assets.planks_oak))

    Block.register_block('quartz_block_side', IsotropicBlock(Assets.quartz_block_side))
    Block.register_block('quartz_ore', IsotropicBlock(Assets.quartz_ore))
    Block.register_block('redstone_block', IsotropicBlock(Assets.redstone_block))
    Block.register_block('redstone_ore', IsotropicBlock(Assets.redstone_ore))
    Block.register_block('red_sand', IsotropicBlock(Assets.red_sand))
    Block.register_block('sand', IsotropicBlock(Assets.sand))
    Block.register_block('stone', IsotropicBlock(Assets.stone))
    Block.register_block('stonebrick', IsotropicBlock(Assets.stonebrick))
    Block.register_block('stonebrick_carved', IsotropicBlock(Assets.stonebrick_carved))
    Block.register_block('stonebrick_cracked', IsotropicBlock(Assets.stonebrick_cracked))
    Block.register_block('stonebrick_mossy', IsotropicBlock(Assets.stonebrick_mossy))
    Block.register_block('stone_slab_side', IsotropicBlock(Assets.stone_slab_side))
    Block.register_block('wool_colored_black', IsotropicBlock(Assets.wool_colored_black))
    Block.register_block('wool_colored_blue', IsotropicBlock(Assets.wool_colored_blue))
    Block.register_block('wool_colored_brown', IsotropicBlock(Assets.wool_colored_brown))
    Block.register_block('wool_colored_cyan', IsotropicBlock(Assets.wool_colored_cyan))
    Block.register_block('wool_colored_gray', IsotropicBlock(Assets.wool_colored_gray))
    Block.register_block('wool_colored_green', IsotropicBlock(Assets.wool_colored_green))
    Block.register_block('wool_colored_light_blue', IsotropicBlock(Assets.wool_colored_light_blue))
    Block.register_block('wool_colored_lime', IsotropicBlock(Assets.wool_colored_lime))
    Block.register_block('wool_colored_magenta', IsotropicBlock(Assets.wool_colored_magenta))
    Block.register_block('wool_colored_orange', IsotropicBlock(Assets.wool_colored_orange))
    Block.register_block('wool_colored_pink', IsotropicBlock(Assets.wool_colored_pink))
    Block.register_block('wool_colored_purple', IsotropicBlock(Assets.wool_colored_purple))
    Block.register_block('wool_colored_red', IsotropicBlock(Assets.wool_colored_red))
    Block.register_block('wool_colored_silver', IsotropicBlock(Assets.wool_colored_silver))
    Block.register_block('wool_colored_white', IsotropicBlock(Assets.wool_colored_white))
    Block.register_block('wool_colored_yellow', IsotropicBlock(Assets.wool_colored_yellow))

    # block

    Block.register_block('grass', Block(texture=Assets.grass, sound_name_on_destroy='dig-grass1'))
    Block.register_block('tnt', Block(texture=Assets.tnt, sound_name_on_destroy='dig-grass1'))

    from block.blocks.torch import Torch
    Block.register_block('torch', Torch())

    from block.blocks.log import Log
    Block.register_block('log_big_oak', Log(Assets.log_big_oak))
    Block.register_block('log_birch', Log(Assets.log_birch))
    Block.register_block('log_oak', Log(Assets.log_oak))
    Block.register_block('log_jungle', Log(Assets.log_jungle))
    Block.register_block('log_spruce', Log(Assets.log_spruce))

    Block.register_block('sandstone_carved', Block(model=Assets.block, texture=Assets.sandstone_carved))
    Block.register_block('sandstone_normal', Block(model=Assets.block, texture=Assets.sandstone_normal))
    Block.register_block('sandstone_smooth', Block(model=Assets.block, texture=Assets.sandstone_smooth))

    from block.blocks.piston import Piston
    from block.blocks.piston import StickPiston
    Block.register_block('piston', Piston())
    Block.register_block('stick_piston', StickPiston())

    from block.blocks.endframe import EndFrame
    Block.register_block('endframe', EndFrame())

    from block.blocks.enchanting_table import EnchantingTable
    Block.register_block('enchanting_table', EnchantingTable())

    from block.blocks.fence_door import FenceDoor
    Block.register_block('fence_door', FenceDoor())






