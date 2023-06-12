from direct.actor.Actor import Actor
from ursina import Ursina, held_keys, mouse, Vec3, camera, scene, window, color, InputField, Audio, Entity, destroy, \
    Sequence, Func, curve, load_model

from assets import AssetsManager, Assets
from block.block import place_prototype_block
from block.block_importer import init_blocks
from etale.client import client
from item.item_importer import init_items, shortcut_block
from level.level import Level

app = Ursina(development_mode=True)

# rgba(172, 210, 255, 1)
window.color = color.rgba(0.67, 0.82, 1, 1)

init_blocks()
init_items()

AssetsManager.load_sounds()
AssetsManager.load_music()

AssetsManager.start_music_queue()

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


class EmbedEntity(Entity):

    def __init__(self, model, position):
        super().__init__(model=model, position=position)

    def on_click(self):
        destroy(self)


half_duration = 2
offset = (0, 1, 0)


class Paimon(EmbedEntity):

    def __init__(self, model, position):
        super().__init__(model, position + (0, 1, 0))

        self.lift_animate()
        sequence = Sequence(Func(self.lift_animate), duration=half_duration * 2, loop=True)
        sequence.start()

    def lift_animate(self):
        pos = self.position + offset
        seq = self.animate_position(
            value=pos,
            duration=half_duration,
            curve=curve.in_out_quad,
        )[0]

        seq.append(Func(lambda: self.animate_position(
            value=pos - offset,
            duration=half_duration,
            curve=curve.in_out_quad
        )))


# kuki = embed_model('mods/genshin/models/kuki', Vec3(-2, 2, 4))
# kuki.scale = 0.15

paimon = Paimon('mods/genshin/models/paimon', Vec3(0, 2, 4))
paimon.scale = 0.2

# babara = embed_model('mods/genshin/models/babara', Vec3(2, 2, 4))
# babara.scale = 0.15


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
        Level.set_block(identifier, (x - 10, y, 15))

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
