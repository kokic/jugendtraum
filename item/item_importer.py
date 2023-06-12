from direct.actor.Actor import Actor
from ursina import Entity, Vec3, destroy, load_model

from assets import Assets
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

    Item.register_item('apple', Item(Assets.apple))
    Item.register_item('apple_golden', Item(Assets.apple_golden))
    Item.register_item('arrow', Item(Assets.arrow))
    Item.register_item('bed_red', Item(Assets.bed_red))
    Item.register_item('beef_cooked', Item(Assets.beef_cooked))
    Item.register_item('beef_raw', Item(Assets.beef_raw))
    Item.register_item('blaze_powder', Item(Assets.blaze_powder))
    Item.register_item('blaze_rod', Item(Assets.blaze_rod))
    Item.register_item('boat', Item(Assets.boat))
    Item.register_item('boat_acacia', Item(Assets.boat_acacia))
    Item.register_item('boat_birch', Item(Assets.boat_birch))
    Item.register_item('bone', Item(Assets.bone))
    Item.register_item('book_enchanted', Item(Assets.book_enchanted))
    Item.register_item('book_normal', Item(Assets.book_normal))
    Item.register_item('book_portfolio', Item(Assets.book_portfolio))
    Item.register_item('book_writable', Item(Assets.book_writable))
    Item.register_item('book_written', Item(Assets.book_written))
    Item.register_item('bow_standby', Item(Assets.bow_standby))
    Item.register_item('bread', Item(Assets.bread))
    Item.register_item('brewing_stand', Item(Assets.brewing_stand))
    Item.register_item('bucket_lava', Item(Assets.bucket_lava))
    Item.register_item('bucket_milk', Item(Assets.bucket_milk))
    Item.register_item('bucket_water', Item(Assets.bucket_water))
    Item.register_item('cake', Item(Assets.cake))
    Item.register_item('carrot', Item(Assets.carrot))
    Item.register_item('carrot_golden', Item(Assets.carrot_golden))
    Item.register_item('carrot_on_a_stick', Item(Assets.carrot_on_a_stick))
    Item.register_item('cauldron', Item(Assets.cauldron))
    Item.register_item('chicken_cooked', Item(Assets.chicken_cooked))
    Item.register_item('chicken_raw', Item(Assets.chicken_raw))
    Item.register_item('diamond', Item(Assets.diamond))
    Item.register_item('diamond_axe', Item(Assets.diamond_axe))
    Item.register_item('diamond_boots', Item(Assets.diamond_boots))
    Item.register_item('diamond_chestplate', Item(Assets.diamond_chestplate))
    Item.register_item('diamond_helmet', Item(Assets.diamond_helmet))
    Item.register_item('diamond_hoe', Item(Assets.diamond_hoe))
    Item.register_item('diamond_leggings', Item(Assets.diamond_leggings))
    Item.register_item('diamond_pickaxe', Item(Assets.diamond_pickaxe))
    Item.register_item('diamond_shovel', Item(Assets.diamond_shovel))
    Item.register_item('diamond_sword', Item(Assets.diamond_sword))
    Item.register_item('dye_powder_white', Item(Assets.dye_powder_white))
    Item.register_item('egg', Item(Assets.egg))
    Item.register_item('egg_bat', Item(Assets.egg_bat))
    Item.register_item('egg_blaze', Item(Assets.egg_blaze))
    Item.register_item('egg_cave_spider', Item(Assets.egg_cave_spider))
    Item.register_item('egg_chicken', Item(Assets.egg_chicken))
    Item.register_item('egg_cow', Item(Assets.egg_cow))
    Item.register_item('egg_creeper', Item(Assets.egg_creeper))
    Item.register_item('egg_donkey', Item(Assets.egg_donkey))
    Item.register_item('egg_enderman', Item(Assets.egg_enderman))
    Item.register_item('egg_endermite', Item(Assets.egg_endermite))
    Item.register_item('egg_ghast', Item(Assets.egg_ghast))
    Item.register_item('egg_guardian', Item(Assets.egg_guardian))
    Item.register_item('egg_horse', Item(Assets.egg_horse))
    Item.register_item('egg_husk', Item(Assets.egg_husk))
    Item.register_item('egg_lava_slime', Item(Assets.egg_lava_slime))
    Item.register_item('egg_mule', Item(Assets.egg_mule))
    Item.register_item('egg_mushroomcow', Item(Assets.egg_mushroomcow))
    Item.register_item('egg_ocelot', Item(Assets.egg_ocelot))
    Item.register_item('egg_pig', Item(Assets.egg_pig))
    Item.register_item('egg_pigzombie', Item(Assets.egg_pigzombie))
    Item.register_item('egg_rabbit', Item(Assets.egg_rabbit))
    Item.register_item('egg_sheep', Item(Assets.egg_sheep))
    Item.register_item('egg_silverfish', Item(Assets.egg_silverfish))
    Item.register_item('egg_skeleton', Item(Assets.egg_skeleton))
    Item.register_item('egg_skeletonhorse', Item(Assets.egg_skeletonhorse))
    Item.register_item('egg_slime', Item(Assets.egg_slime))
    Item.register_item('egg_spider', Item(Assets.egg_spider))
    Item.register_item('egg_squid', Item(Assets.egg_squid))
    Item.register_item('egg_stray', Item(Assets.egg_stray))
    Item.register_item('egg_villager', Item(Assets.egg_villager))
    Item.register_item('egg_witch', Item(Assets.egg_witch))
    Item.register_item('egg_wither', Item(Assets.egg_wither))
    Item.register_item('egg_wolf', Item(Assets.egg_wolf))
    Item.register_item('egg_zombie', Item(Assets.egg_zombie))
    Item.register_item('egg_zombiehorse', Item(Assets.egg_zombiehorse))
    Item.register_item('ender_eye', Item(Assets.ender_eye))
    Item.register_item('ender_pearl', Item(Assets.ender_pearl))
    Item.register_item('experience_bottle', Item(Assets.experience_bottle))
    Item.register_item('fireball', Item(Assets.fireball))
    Item.register_item('fireworks', Item(Assets.fireworks))
    Item.register_item('fish_clownfish_raw', Item(Assets.fish_clownfish_raw))
    Item.register_item('fish_cooked', Item(Assets.fish_cooked))
    Item.register_item('fish_pufferfish_raw', Item(Assets.fish_pufferfish_raw))
    Item.register_item('fish_raw', Item(Assets.fish_raw))
    Item.register_item('fish_salmon_cooked', Item(Assets.fish_salmon_cooked))
    Item.register_item('fish_salmon_raw', Item(Assets.fish_salmon_raw))
    Item.register_item('flint', Item(Assets.flint))
    Item.register_item('flint_and_steel', Item(Assets.flint_and_steel))
    Item.register_item('iron_axe', Item(Assets.iron_axe))
    Item.register_item('iron_hoe', Item(Assets.iron_hoe))
    Item.register_item('iron_pickaxe', Item(Assets.iron_pickaxe))
    Item.register_item('iron_shovel', Item(Assets.iron_shovel))
    Item.register_item('iron_sword', Item(Assets.iron_sword))
    Item.register_item('lever', Item(Assets.lever))
    Item.register_item('potato', Item(Assets.potato))
    Item.register_item('seeds_wheat', Item(Assets.seeds_wheat))
    Item.register_item('wheat', Item(Assets.wheat))

    # binds

    Item.items['carrot'].use_on = shortcut_block(
        AssetsManager.get_model_path('surround'),
        AssetsManager.get_blocks_path('carrots_stage_3')
    )

    Item.items['potato'].use_on = shortcut_block(
        AssetsManager.get_model_path('surround'),
        AssetsManager.get_blocks_path('potatoes_stage_3')
    )

    Item.items['seeds_wheat'].use_on = shortcut_block(
        AssetsManager.get_model_path('surround'),
        AssetsManager.get_blocks_path('wheat_stage_7')
    )

    Item.items['dye_powder_white'].use_on = shortcut_block(
        AssetsManager.get_model_path('surround'),
        AssetsManager.get_blocks_path('double_plant_grass_carried')
    )

    Item.items['ender_eye'].use_on = ender_eye_use_on

    Item.items['egg_pig'].use_on = spawn_pig
    Item.items['egg_cow'].use_on = shortcut_mob('cow/cow')

    Item.items['egg_zombie'].use_on = spawn_zombie
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


def spawn_pig(ins, data, target):
    pig = Entity(position=target.position + Vec3(0, 0.5, 0))
    pig.rotation_y = 180
    pig.collider = 'box'
    pig.on_click = lambda: destroy(pig)

    pig.actor = Actor(models=Assets.pig)
    pig.actor.reparent_to(pig)
    pig.actor.loop("animation.pig.walk")
    return pig


def spawn_zombie(ins, data, target):
    zombie = EntityFactory.mob('zombie/zombie', target.position + Vec3(0, 0.5, 0))
    # bug
    zombie.input = lambda key: zombie_input(zombie, key)


def zombie_input(entity: Entity, key):
    if key == 'm':
        EntityFactory.mob('mutant-zombie/mutant-zombie', entity.position)
        destroy(entity)


def ender_eye_use_on(instance: ItemInstance, data, target: Entity):
    if data.identifier == 'endframe' and not target.eye.enabled:
        target.eye.enable()
