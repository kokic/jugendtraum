from ursina import Entity, Vec3, destroy

from block.block import place_prototype_block
from entity.entity import EntityFactory
from item.item import Item, ItemInstance


def init_items():
    # import os
    #
    # for filename in os.listdir(AssetsManager.get_items_path('')):
    #     texture = AssetsManager.get_items_path(filename)
    #     identifier = filename[:-4]
    #     Item.register_item(identifier, Item(texture))

    from assets import Assets
    from assets import AssetsManager

    Item.register_item('bedrock', Item(Assets.bedrock))
    Item.register_item('brick', Item(Assets.brick))
    Item.register_item('coal_ore', Item(Assets.coal_ore))
    Item.register_item('cobblestone', Item(Assets.cobblestone))
    Item.register_item('cobblestone_mossy', Item(Assets.cobblestone_mossy))
    Item.register_item('command_block', Item(Assets.command_block))
    Item.register_item('concrete_black', Item(Assets.concrete_black))
    Item.register_item('concrete_blue', Item(Assets.concrete_blue))
    Item.register_item('concrete_brown', Item(Assets.concrete_brown))
    Item.register_item('concrete_cyan', Item(Assets.concrete_cyan))
    Item.register_item('concrete_gray', Item(Assets.concrete_gray))
    Item.register_item('concrete_green', Item(Assets.concrete_green))
    Item.register_item('concrete_light_blue', Item(Assets.concrete_light_blue))
    Item.register_item('concrete_lime', Item(Assets.concrete_lime))
    Item.register_item('concrete_magenta', Item(Assets.concrete_magenta))
    Item.register_item('concrete_orange', Item(Assets.concrete_orange))
    Item.register_item('concrete_pink', Item(Assets.concrete_pink))
    Item.register_item('concrete_purple', Item(Assets.concrete_purple))
    Item.register_item('concrete_red', Item(Assets.concrete_red))
    Item.register_item('concrete_silver', Item(Assets.concrete_silver))
    Item.register_item('concrete_white', Item(Assets.concrete_white))
    Item.register_item('concrete_yellow', Item(Assets.concrete_yellow))
    Item.register_item('diamond_block', Item(Assets.diamond_block))
    Item.register_item('diamond_ore', Item(Assets.diamond_ore))
    Item.register_item('dirt', Item(Assets.dirt))
    Item.register_item('emerald_block', Item(Assets.emerald_block))
    Item.register_item('ender_chest_front', Item(Assets.ender_chest_front))
    Item.register_item('ender_chest_side', Item(Assets.ender_chest_side))
    Item.register_item('ender_chest_top', Item(Assets.ender_chest_top))
    Item.register_item('end_stone', Item(Assets.end_stone))
    Item.register_item('glowing_obsidian', Item(Assets.glowing_obsidian))
    Item.register_item('glowstone', Item(Assets.glowstone))
    Item.register_item('gold_block', Item(Assets.gold_block))
    Item.register_item('gold_ore', Item(Assets.gold_ore))
    Item.register_item('gravel', Item(Assets.gravel))
    Item.register_item('iron_block', Item(Assets.iron_block))
    Item.register_item('iron_ore', Item(Assets.iron_ore))
    Item.register_item('lapis_ore', Item(Assets.lapis_ore))
    Item.register_item('mob_spawner', Item(Assets.mob_spawner))
    Item.register_item('nether_brick', Item(Assets.nether_brick))
    Item.register_item('planks_acacia', Item(Assets.planks_acacia))
    Item.register_item('planks_big_oak', Item(Assets.planks_big_oak))
    Item.register_item('planks_birch', Item(Assets.planks_birch))
    Item.register_item('planks_jungle', Item(Assets.planks_jungle))
    Item.register_item('planks_oak', Item(Assets.planks_oak))
    Item.register_item('planks_spruce', Item(Assets.planks_spruce))
    Item.register_item('quartz_block_side', Item(Assets.quartz_block_side))
    Item.register_item('quartz_ore', Item(Assets.quartz_ore))
    Item.register_item('redstone_block', Item(Assets.redstone_block))
    Item.register_item('redstone_ore', Item(Assets.redstone_ore))
    Item.register_item('red_sand', Item(Assets.red_sand))
    Item.register_item('sand', Item(Assets.sand))
    Item.register_item('stone', Item(Assets.stone))
    Item.register_item('stonebrick', Item(Assets.stonebrick))
    Item.register_item('stonebrick_carved', Item(Assets.stonebrick_carved))
    Item.register_item('stonebrick_cracked', Item(Assets.stonebrick_cracked))
    Item.register_item('stonebrick_mossy', Item(Assets.stonebrick_mossy))
    Item.register_item('stone_slab_side', Item(Assets.stone_slab_side))
    Item.register_item('wool_colored_black', Item(Assets.wool_colored_black))
    Item.register_item('wool_colored_blue', Item(Assets.wool_colored_blue))
    Item.register_item('wool_colored_brown', Item(Assets.wool_colored_brown))
    Item.register_item('wool_colored_cyan', Item(Assets.wool_colored_cyan))
    Item.register_item('wool_colored_gray', Item(Assets.wool_colored_gray))
    Item.register_item('wool_colored_green', Item(Assets.wool_colored_green))
    Item.register_item('wool_colored_light_blue', Item(Assets.wool_colored_light_blue))
    Item.register_item('wool_colored_lime', Item(Assets.wool_colored_lime))
    Item.register_item('wool_colored_magenta', Item(Assets.wool_colored_magenta))
    Item.register_item('wool_colored_orange', Item(Assets.wool_colored_orange))
    Item.register_item('wool_colored_pink', Item(Assets.wool_colored_pink))
    Item.register_item('wool_colored_purple', Item(Assets.wool_colored_purple))
    Item.register_item('wool_colored_red', Item(Assets.wool_colored_red))
    Item.register_item('wool_colored_silver', Item(Assets.wool_colored_silver))
    Item.register_item('wool_colored_white', Item(Assets.wool_colored_white))
    Item.register_item('wool_colored_yellow', Item(Assets.wool_colored_yellow))

    # binds

    Item.items['carrot'].use_on = shortcut_block(
        AssetsManager.get_model('surround'),
        AssetsManager.get_blocks_path('carrots_stage_3')
    )

    Item.items['potato'].use_on = shortcut_block(
        AssetsManager.get_model('surround'),
        AssetsManager.get_blocks_path('potatoes_stage_3')
    )

    Item.items['seeds_wheat'].use_on = shortcut_block(
        AssetsManager.get_model('surround'),
        AssetsManager.get_blocks_path('wheat_stage_7')
    )

    Item.items['dye_powder_white'].use_on = shortcut_block(
        AssetsManager.get_model('surround'),
        AssetsManager.get_blocks_path('double_plant_grass_carried')
    )

    Item.items['ender_eye'].use_on = ender_eye_use_on

    Item.items['egg_pig'].use_on = shortcut_mob('pig/pig')
    Item.items['egg_cow'].use_on = shortcut_mob('cow/cow')

    Item.items['egg_creeper'].use_on = shortcut_mob('creeper/creeper')
    Item.items['egg_skeleton'].use_on = shortcut_mob('skeleton/skeleton')

    Item.items['egg_ghast'].use_on = shortcut_mob('ghast/ghast')


def shortcut_block(model, texture):

    def generator(ins, data, target):
        position = target.position + Vec3(0, 0.5, 0)
        block = place_prototype_block(model, texture, position)
        block.collider = 'mesh'
        block.on_click = lambda: destroy(block)

    return generator


def shortcut_mob(name):
    return lambda ins, data, target: \
        EntityFactory.mob(name, target.position + Vec3(0, 0.5, 0))


def ender_eye_use_on(instance: ItemInstance, data, target: Entity):
    if data.identifier == 'endframe' and not target.eye.enabled:
        target.eye.enable()
