from ursina import Entity, Vec3, destroy

from block.block import place_prototype_block
from entity.entity import EntityFactory
from item.item import Item, ItemInstance


def init_items():
    import os
    from assets import AssetsManager

    for filename in os.listdir(AssetsManager.get_items_path('')):
        texture = AssetsManager.get_items_path(filename)
        identifier = filename[:-4]
        Item.register_item(identifier, Item(texture))

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
