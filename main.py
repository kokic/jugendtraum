from ursina import Ursina, held_keys, mouse, Vec3, camera, scene, window, color, InputField

from block.block_importer import init_blocks
from etale.client import client
from item.item_importer import init_items
from level.level import Level

app = Ursina(development_mode=True)

# rgba(172, 210, 255, 1)
window.color = color.rgba(0.67, 0.82, 1, 1)

init_blocks()
init_items()

#
generate_grass_ground = True
show_woolen_code = False
#

if generate_grass_ground:
    for x in range(-4, 4):
        for z in range(8):
            Level.set_block('grass', (x, 1, z))

Level.set_block('dirt', (-2, 2, 2))
Level.set_block('endframe', (-1, 2, 2))
Level.set_block('enchanting_table', (0, 2, 2))
Level.set_block('fence_door', (1, 2, 2))

#
# from PIL import Image
#
# codeImage = Image.open('F:/minecraft-dev/g3fi/code.png')
#
# pixels = list(codeImage.getdata())
# pixels = map(lambda x: 0 if x[0] == 0 else 1, pixels)
# print(list(pixels))

codePixels = [
    0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1,
    1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0,
    1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0
]

if show_woolen_code:
    for index, value in enumerate(codePixels):
        x = index % 21
        y = 21 - index // 21
        identifier = 'wool_colored_black' if value == 0 else 'wool_colored_white'
        Level.set_block(identifier, (x, y, 5))

client.load()

# EndFrame(position=(3, 2, 2))
# EnchantingTable(position=(4, 2, 2))
# FenceDoor(position=(5, 2, 2))

player = client.player
player.gravity = 0
player.y = 1.5


def update():
    if held_keys['space']:
        player.y += 0.2
    if held_keys['shift']:
        player.y -= 0.2

    client.inventory_ui.mouse_selected.position = mouse.position - Vec3(0.005, 0.005, 0)


command_input = InputField()
command_input.disable()


def input(key):
    # print(key)
    if key == 'escape':
        if client.inventory_ui.enabled:
            client.inventory_ui.disable()
        else:
            from ursina import application
            application.quit()

    # if key == '/':
    #     client.player.disable()
    #     command_input.enable()
    #
    # if key == 'enter' and command_input.enabled:
    #     command_input.disable()
    #     print(command_input.text)

    if key == 'o':
        mouse.locked = False

    if key == 'g':
        player.gravity = 1 - player.gravity

    if key == 'scroll up':
        client.hotbar_ui.move_selector(-1)

    if key == 'scroll down':
        client.hotbar_ui.move_selector()

    if key == 'e':
        if client.inventory_ui.enabled:
            client.inventory_ui.disable()
        else:
            client.inventory_ui.enable()


app.run()
