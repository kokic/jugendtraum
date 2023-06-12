import math
import os
import random

from PIL import Image
from ursina import Texture, color, Audio, Sequence, Func, Wait, load_model


# from PIL import Image
# Image.new('RGBA', (48, 16), color=(0, 0, 0, 0)).save('block.png')


class AssetsManager:

    @staticmethod
    def get_sound_path(name):
        return f"sound/{name}"

    @staticmethod
    def get_music_path(name):
        return f"music/{name}"

    @staticmethod
    def get_model_path(name):
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
    def block_texture_2(name) -> Texture:
        return AssetsManager.block_texture_32x16(
            f"{name}_top.png",
            f"{name}_side.png"
        )

    @staticmethod
    def block_texture_32x16(top, side) -> Texture:
        top_image = Image.open(AssetsManager.get_blocks_path(top))
        side_image = Image.open(AssetsManager.get_blocks_path(side))
        image = Image.open('images/empty_32x16.png')
        image.paste(top_image, (0, 0))
        image.paste(side_image, (16, 0))
        return Texture(image)

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

    # sound

    __sounds: dict[str, Audio] = {}

    @staticmethod
    def load_sounds():
        for filename in os.listdir(AssetsManager.get_sound_path('')):
            name = filename[:-4]
            path = AssetsManager.get_sound_path(name)
            AssetsManager.__sounds[name] = Audio(path, autoplay=False)

    @staticmethod
    def get_sound(name) -> Audio:
        return AssetsManager.__sounds[name]

    # animations
    @staticmethod
    def random_background_sound():
        pass

    # music

    __music: dict[str, Audio] = {}
    __music_duration = 0

    @staticmethod
    def load_music():

        for filename in os.listdir(AssetsManager.get_music_path('')):
            name = filename[:-4]
            path = AssetsManager.get_music_path(name)
            music = Audio(path, autoplay=False)
            AssetsManager.__music[name] = music
            AssetsManager.__music_duration += music.length

    @staticmethod
    def get_music(name) -> Audio:
        return AssetsManager.__music[name]

    @staticmethod
    def once_music_queue():

        # # genshin
        # twilight_serenity = AssetsManager.get_music('Twilight Serenity')
        # journey_of_hope = AssetsManager.get_music('Journey of Hope')
        # genshin_impact_main_theme = AssetsManager.get_music('Genshin Impact Main Theme')
        # rapid_as_wildfires = AssetsManager.get_music('Rapid as Wildfires')
        # gallant_challenge = AssetsManager.get_music('Gallant Challenge')
        #
        # # minecraft
        # minecraft = AssetsManager.get_music('Minecraft')
        # clark = AssetsManager.get_music('Clark')

        # generate random sequence
        sequence = Sequence()

        music_keys = list(AssetsManager.__music.keys())
        random.shuffle(music_keys)
        print(music_keys)

        for n in range(0, len(music_keys)):
            music = AssetsManager.__music[music_keys[n]]
            sequence.append(Func(music.play))
            sequence.append(math.ceil(music.length))

        # sequence = Sequence(Func(twilight_serenity.play))
        # sequence.append(math.ceil(twilight_serenity.length))
        #
        # sequence.append(Func(journey_of_hope.play))
        # sequence.append(math.ceil(journey_of_hope.length))
        #
        # sequence.append(Func(clark.play))
        # sequence.append(math.ceil(clark.length))

        sequence.start()
        return sequence

    @staticmethod
    def start_music_queue():
        AssetsManager.once_music_queue()
        sequence = Sequence(
            Func(AssetsManager.once_music_queue),
            duration=AssetsManager.__music_duration,
            loop=True
        )
        sequence.start()
        return sequence


def shortcut_log_texture(name):
    return AssetsManager.block_texture_32x16(
        f"log_{name}_top.png",
        f"log_{name}.png"
    )


# JSON
class Assets:
    # models
    dropping = AssetsManager.get_model_path('dropping')
    isotropic = AssetsManager.get_model_path('isotropic')
    block = AssetsManager.get_model_path('block')
    log = AssetsManager.get_model_path('log')
    slab = AssetsManager.get_model_path('slab')

    # mob animation model
    pig = load_model("models/mob/pig/pig.gltf")

    # torch = AssetsManager.get_model('torch/torch')

    # item texture
    empty = Texture(Image.new('RGBA', (16, 16), color=(0, 0, 0, 0)))
    apple = AssetsManager.get_items_path('apple.png')
    apple_golden = AssetsManager.get_items_path('apple_golden.png')
    arrow = AssetsManager.get_items_path('arrow.png')
    bed_red = AssetsManager.get_items_path('bed_red.png')
    beef_cooked = AssetsManager.get_items_path('beef_cooked.png')
    beef_raw = AssetsManager.get_items_path('beef_raw.png')
    blaze_powder = AssetsManager.get_items_path('blaze_powder.png')
    blaze_rod = AssetsManager.get_items_path('blaze_rod.png')
    boat = AssetsManager.get_items_path('boat.png')
    boat_acacia = AssetsManager.get_items_path('boat_acacia.png')
    boat_birch = AssetsManager.get_items_path('boat_birch.png')
    bone = AssetsManager.get_items_path('bone.png')
    book_enchanted = AssetsManager.get_items_path('book_enchanted.png')
    book_normal = AssetsManager.get_items_path('book_normal.png')
    book_portfolio = AssetsManager.get_items_path('book_portfolio.png')
    book_writable = AssetsManager.get_items_path('book_writable.png')
    book_written = AssetsManager.get_items_path('book_written.png')
    bow_standby = AssetsManager.get_items_path('bow_standby.png')
    bread = AssetsManager.get_items_path('bread.png')
    brewing_stand = AssetsManager.get_items_path('brewing_stand.png')
    bucket_lava = AssetsManager.get_items_path('bucket_lava.png')
    bucket_milk = AssetsManager.get_items_path('bucket_milk.png')
    bucket_water = AssetsManager.get_items_path('bucket_water.png')
    cake = AssetsManager.get_items_path('cake.png')
    carrot = AssetsManager.get_items_path('carrot.png')
    carrot_golden = AssetsManager.get_items_path('carrot_golden.png')
    carrot_on_a_stick = AssetsManager.get_items_path('carrot_on_a_stick.png')
    cauldron = AssetsManager.get_items_path('cauldron.png')
    chicken_cooked = AssetsManager.get_items_path('chicken_cooked.png')
    chicken_raw = AssetsManager.get_items_path('chicken_raw.png')
    diamond = AssetsManager.get_items_path('diamond.png')
    diamond_axe = AssetsManager.get_items_path('diamond_axe.png')
    diamond_boots = AssetsManager.get_items_path('diamond_boots.png')
    diamond_chestplate = AssetsManager.get_items_path('diamond_chestplate.png')
    diamond_helmet = AssetsManager.get_items_path('diamond_helmet.png')
    diamond_hoe = AssetsManager.get_items_path('diamond_hoe.png')
    diamond_leggings = AssetsManager.get_items_path('diamond_leggings.png')
    diamond_pickaxe = AssetsManager.get_items_path('diamond_pickaxe.png')
    diamond_shovel = AssetsManager.get_items_path('diamond_shovel.png')
    diamond_sword = AssetsManager.get_items_path('diamond_sword.png')
    dye_powder_white = AssetsManager.get_items_path('dye_powder_white.png')
    egg = AssetsManager.get_items_path('egg.png')
    egg_bat = AssetsManager.get_items_path('egg_bat.png')
    egg_blaze = AssetsManager.get_items_path('egg_blaze.png')
    egg_cave_spider = AssetsManager.get_items_path('egg_cave_spider.png')
    egg_chicken = AssetsManager.get_items_path('egg_chicken.png')
    egg_cow = AssetsManager.get_items_path('egg_cow.png')
    egg_creeper = AssetsManager.get_items_path('egg_creeper.png')
    egg_donkey = AssetsManager.get_items_path('egg_donkey.png')
    egg_enderman = AssetsManager.get_items_path('egg_enderman.png')
    egg_endermite = AssetsManager.get_items_path('egg_endermite.png')
    egg_ghast = AssetsManager.get_items_path('egg_ghast.png')
    egg_guardian = AssetsManager.get_items_path('egg_guardian.png')
    egg_horse = AssetsManager.get_items_path('egg_horse.png')
    egg_husk = AssetsManager.get_items_path('egg_husk.png')
    egg_lava_slime = AssetsManager.get_items_path('egg_lava_slime.png')
    egg_mule = AssetsManager.get_items_path('egg_mule.png')
    egg_mushroomcow = AssetsManager.get_items_path('egg_mushroomcow.png')
    egg_ocelot = AssetsManager.get_items_path('egg_ocelot.png')
    egg_pig = AssetsManager.get_items_path('egg_pig.png')
    egg_pigzombie = AssetsManager.get_items_path('egg_pigzombie.png')
    egg_rabbit = AssetsManager.get_items_path('egg_rabbit.png')
    egg_sheep = AssetsManager.get_items_path('egg_sheep.png')
    egg_silverfish = AssetsManager.get_items_path('egg_silverfish.png')
    egg_skeleton = AssetsManager.get_items_path('egg_skeleton.png')
    egg_skeletonhorse = AssetsManager.get_items_path('egg_skeletonhorse.png')
    egg_slime = AssetsManager.get_items_path('egg_slime.png')
    egg_spider = AssetsManager.get_items_path('egg_spider.png')
    egg_squid = AssetsManager.get_items_path('egg_squid.png')
    egg_stray = AssetsManager.get_items_path('egg_stray.png')
    egg_villager = AssetsManager.get_items_path('egg_villager.png')
    egg_witch = AssetsManager.get_items_path('egg_witch.png')
    egg_wither = AssetsManager.get_items_path('egg_wither.png')
    egg_wolf = AssetsManager.get_items_path('egg_wolf.png')
    egg_zombie = AssetsManager.get_items_path('egg_zombie.png')
    egg_zombiehorse = AssetsManager.get_items_path('egg_zombiehorse.png')
    ender_eye = AssetsManager.get_items_path('ender_eye.png')
    ender_pearl = AssetsManager.get_items_path('ender_pearl.png')
    experience_bottle = AssetsManager.get_items_path('experience_bottle.png')
    fireball = AssetsManager.get_items_path('fireball.png')
    fireworks = AssetsManager.get_items_path('fireworks.png')
    fish_clownfish_raw = AssetsManager.get_items_path('fish_clownfish_raw.png')
    fish_cooked = AssetsManager.get_items_path('fish_cooked.png')
    fish_pufferfish_raw = AssetsManager.get_items_path('fish_pufferfish_raw.png')
    fish_raw = AssetsManager.get_items_path('fish_raw.png')
    fish_salmon_cooked = AssetsManager.get_items_path('fish_salmon_cooked.png')
    fish_salmon_raw = AssetsManager.get_items_path('fish_salmon_raw.png')
    flint = AssetsManager.get_items_path('flint.png')
    flint_and_steel = AssetsManager.get_items_path('flint_and_steel.png')
    iron_axe = AssetsManager.get_items_path('iron_axe.png')
    iron_hoe = AssetsManager.get_items_path('iron_hoe.png')
    iron_pickaxe = AssetsManager.get_items_path('iron_pickaxe.png')
    iron_shovel = AssetsManager.get_items_path('iron_shovel.png')
    iron_sword = AssetsManager.get_items_path('iron_sword.png')
    lever = AssetsManager.get_items_path('lever.png')
    potato = AssetsManager.get_items_path('potato.png')
    seeds_wheat = AssetsManager.get_items_path('seeds_wheat.png')
    wheat = AssetsManager.get_items_path('wheat.png')

    # isotropic block texture
    bedrock = AssetsManager.get_blocks_path('isotropic/bedrock.png')
    brick = AssetsManager.get_blocks_path('isotropic/brick.png')
    coal_ore = AssetsManager.get_blocks_path('isotropic/coal_ore.png')
    cobblestone = AssetsManager.get_blocks_path('isotropic/cobblestone.png')
    cobblestone_mossy = AssetsManager.get_blocks_path('isotropic/cobblestone_mossy.png')
    command_block = AssetsManager.get_blocks_path('isotropic/command_block.png')
    concrete_black = AssetsManager.get_blocks_path('isotropic/concrete_black.png')
    concrete_blue = AssetsManager.get_blocks_path('isotropic/concrete_blue.png')
    concrete_brown = AssetsManager.get_blocks_path('isotropic/concrete_brown.png')
    concrete_cyan = AssetsManager.get_blocks_path('isotropic/concrete_cyan.png')
    concrete_gray = AssetsManager.get_blocks_path('isotropic/concrete_gray.png')
    concrete_green = AssetsManager.get_blocks_path('isotropic/concrete_green.png')
    concrete_light_blue = AssetsManager.get_blocks_path('isotropic/concrete_light_blue.png')
    concrete_lime = AssetsManager.get_blocks_path('isotropic/concrete_lime.png')
    concrete_magenta = AssetsManager.get_blocks_path('isotropic/concrete_magenta.png')
    concrete_orange = AssetsManager.get_blocks_path('isotropic/concrete_orange.png')
    concrete_pink = AssetsManager.get_blocks_path('isotropic/concrete_pink.png')
    concrete_purple = AssetsManager.get_blocks_path('isotropic/concrete_purple.png')
    concrete_red = AssetsManager.get_blocks_path('isotropic/concrete_red.png')
    concrete_silver = AssetsManager.get_blocks_path('isotropic/concrete_silver.png')
    concrete_white = AssetsManager.get_blocks_path('isotropic/concrete_white.png')
    concrete_yellow = AssetsManager.get_blocks_path('isotropic/concrete_yellow.png')
    diamond_block = AssetsManager.get_blocks_path('isotropic/diamond_block.png')
    diamond_ore = AssetsManager.get_blocks_path('isotropic/diamond_ore.png')
    dirt = AssetsManager.get_blocks_path('isotropic/dirt.png')
    emerald_block = AssetsManager.get_blocks_path('isotropic/emerald_block.png')
    ender_chest_front = AssetsManager.get_blocks_path('isotropic/ender_chest_front.png')
    ender_chest_side = AssetsManager.get_blocks_path('isotropic/ender_chest_side.png')
    ender_chest_top = AssetsManager.get_blocks_path('isotropic/ender_chest_top.png')
    end_stone = AssetsManager.get_blocks_path('isotropic/end_stone.png')
    glowing_obsidian = AssetsManager.get_blocks_path('isotropic/glowing_obsidian.png')
    glowstone = AssetsManager.get_blocks_path('isotropic/glowstone.png')
    gold_block = AssetsManager.get_blocks_path('isotropic/gold_block.png')
    gold_ore = AssetsManager.get_blocks_path('isotropic/gold_ore.png')
    gravel = AssetsManager.get_blocks_path('isotropic/gravel.png')
    iron_block = AssetsManager.get_blocks_path('isotropic/iron_block.png')
    iron_ore = AssetsManager.get_blocks_path('isotropic/iron_ore.png')
    lapis_ore = AssetsManager.get_blocks_path('isotropic/lapis_ore.png')
    mob_spawner = AssetsManager.get_blocks_path('isotropic/mob_spawner.png')
    nether_brick = AssetsManager.get_blocks_path('isotropic/nether_brick.png')
    planks_acacia = AssetsManager.get_blocks_path('isotropic/planks_acacia.png')
    planks_big_oak = AssetsManager.get_blocks_path('isotropic/planks_big_oak.png')
    planks_birch = AssetsManager.get_blocks_path('isotropic/planks_birch.png')
    planks_jungle = AssetsManager.get_blocks_path('isotropic/planks_jungle.png')
    planks_oak = AssetsManager.get_blocks_path('isotropic/planks_oak.png')
    planks_spruce = AssetsManager.get_blocks_path('isotropic/planks_spruce.png')
    quartz_block_side = AssetsManager.get_blocks_path('isotropic/quartz_block_side.png')
    quartz_ore = AssetsManager.get_blocks_path('isotropic/quartz_ore.png')
    redstone_block = AssetsManager.get_blocks_path('isotropic/redstone_block.png')
    redstone_ore = AssetsManager.get_blocks_path('isotropic/redstone_ore.png')
    red_sand = AssetsManager.get_blocks_path('isotropic/red_sand.png')
    sand = AssetsManager.get_blocks_path('isotropic/sand.png')
    stone = AssetsManager.get_blocks_path('isotropic/stone.png')
    stonebrick = AssetsManager.get_blocks_path('isotropic/stonebrick.png')
    stonebrick_carved = AssetsManager.get_blocks_path('isotropic/stonebrick_carved.png')
    stonebrick_cracked = AssetsManager.get_blocks_path('isotropic/stonebrick_cracked.png')
    stonebrick_mossy = AssetsManager.get_blocks_path('isotropic/stonebrick_mossy.png')
    stone_slab_side = AssetsManager.get_blocks_path('isotropic/stone_slab_side.png')
    wool_colored_black = AssetsManager.get_blocks_path('isotropic/wool_colored_black.png')
    wool_colored_blue = AssetsManager.get_blocks_path('isotropic/wool_colored_blue.png')
    wool_colored_brown = AssetsManager.get_blocks_path('isotropic/wool_colored_brown.png')
    wool_colored_cyan = AssetsManager.get_blocks_path('isotropic/wool_colored_cyan.png')
    wool_colored_gray = AssetsManager.get_blocks_path('isotropic/wool_colored_gray.png')
    wool_colored_green = AssetsManager.get_blocks_path('isotropic/wool_colored_green.png')
    wool_colored_light_blue = AssetsManager.get_blocks_path('isotropic/wool_colored_light_blue.png')
    wool_colored_lime = AssetsManager.get_blocks_path('isotropic/wool_colored_lime.png')
    wool_colored_magenta = AssetsManager.get_blocks_path('isotropic/wool_colored_magenta.png')
    wool_colored_orange = AssetsManager.get_blocks_path('isotropic/wool_colored_orange.png')
    wool_colored_pink = AssetsManager.get_blocks_path('isotropic/wool_colored_pink.png')
    wool_colored_purple = AssetsManager.get_blocks_path('isotropic/wool_colored_purple.png')
    wool_colored_red = AssetsManager.get_blocks_path('isotropic/wool_colored_red.png')
    wool_colored_silver = AssetsManager.get_blocks_path('isotropic/wool_colored_silver.png')
    wool_colored_white = AssetsManager.get_blocks_path('isotropic/wool_colored_white.png')
    wool_colored_yellow = AssetsManager.get_blocks_path('isotropic/wool_colored_yellow.png')

    # block texture
    grass = AssetsManager.block_texture_48x16(
        'grass_carried.png',
        'grass_side_carried.png',
        'dirt.png'
    )

    log_big_oak = shortcut_log_texture('big_oak')
    log_birch = shortcut_log_texture('birch')
    log_jungle = shortcut_log_texture('jungle')
    log_oak = shortcut_log_texture('oak')
    log_spruce = shortcut_log_texture('spruce')

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
