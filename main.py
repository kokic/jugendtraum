from ursina import Ursina, held_keys, mouse

from block.block import Level, Block
from block.enchanting_table import EnchantingTable
from block.endframe import EndFrame
from block.fence_door import FenceDoor
from block.piston import PistonBlock
from client import client
from gui.hud_screen import HotbarUI

app = Ursina()

Block.init_blocks()

generate_grass_ground = True
#
if generate_grass_ground:
    for x in range(-4, 4):
        for z in range(8):
            Level.set_block('grass', (x, 1, z))


#
# PistonBlock(position=(2, 2, 2))
# EndFrame(position=(3, 2, 2))
# EnchantingTable(position=(4, 2, 2))
# FenceDoor(position=(5, 2, 2))

player = client.player
player.gravity = 0
player.y = 1.5

hotbar = HotbarUI()


#
# Block(position=(1, 2, 2), model='block', texture=AssetsManager.block_texture_3('tnt'))
# Block(position=(2, 2, 2), model='block', texture=AssetsManager.block_texture_48x16(
#     'sandstone_top.png',
#     'sandstone_carved.png',
#     'sandstone_bottom.png'
# ))

def update():
    if held_keys['space']:
        player.y += 0.2
    if held_keys['shift']:
        player.y -= 0.2


def input(key):
    if key == 'escape':
        mouse.locked = False
    if key == 'g':
        player.gravity = 1 - player.gravity

    if key == 'n':
        hotbar.move_selector()


app.run()
