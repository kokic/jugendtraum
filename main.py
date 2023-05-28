from ursina import Ursina, held_keys, mouse

from block.block import Level, Block
from client import client
from gui.hud import HotbarUI
from gui.inventory import InventoryUI

app = Ursina()

Block.init_blocks()

generate_grass_ground = True
#
if generate_grass_ground:
    for x in range(-4, 4):
        for z in range(8):
            Level.set_block('grass', (x, 1, z))

Level.set_block('dirt', (0, 2, 2))

# EndFrame(position=(3, 2, 2))
# EnchantingTable(position=(4, 2, 2))
# FenceDoor(position=(5, 2, 2))

player = client.player
player.gravity = 0
player.y = 1.5

hotbar = HotbarUI()
# inventory = InventoryUI()


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
