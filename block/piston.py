from ursina import curve, Func, Sequence, mouse, Vec3, Entity

from block.block import Block
from client import ViewDirection, get_face_from_normal
from entity.entity import EntityBlock

half_duration = 0.3
# 0.3


push_phase1, push_phase2 = Vec3(0, 0, -0.4), Vec3(0, 0, -1)


# piston-base is a block
# piston-arm is an entity

def fetch_asset(name):
    return f"models/piston/{name}"


def arm_phase2_animate(level_block: Entity, model, position):
    def generator():
        level_block.arm.update_model(fetch_asset(model))
        level_block.arm.collider = 'mesh'

        level_block.arm.animate_position(
            value=position,
            duration=half_duration,
            curve=curve.out_expo
        )

    return generator


class PistonBlock(Block):

    def __init__(self, texture=fetch_asset('piston.png')):
        super().__init__(
            model=fetch_asset('piston-push-base'),
            texture=texture,
        )

        # self.face = ViewDirection.FRONT
        # self.arm = EntityBlock(
        #     fetch_asset('piston-push-arm-0'),
        #     fetch_asset('piston.png'),
        # )
        # self.can_play_animate = True

        # for key, value in kwargs.items():
        #     setattr(self, key, value)

    # def rotate_by_face(self, face: ViewDirection):
    #     if face.back():
    #         self.rotation_y = 180
    #     elif face.left():
    #         self.rotation_y = 90
    #     elif face.right():
    #         self.rotation_y = -90
    #     elif face.top():
    #         self.rotation_x = 90
    #     elif face.bottom():
    #         self.rotation_x = -90

    @staticmethod
    def rotate_by_face(level_block: Entity, face: ViewDirection):
        if face.back():
            level_block.rotation_y = 180
        elif face.left():
            level_block.rotation_y = 90
        elif face.right():
            level_block.rotation_y = -90
        elif face.top():
            level_block.rotation_x = 90
        elif face.bottom():
            level_block.rotation_x = -90

    def place(self, position):
        face = get_face_from_normal(mouse.world_normal)
        level_block = super().place(position)
        PistonBlock.rotate_by_face(level_block, face)

        level_block.arm = EntityBlock(
            fetch_asset('piston-push-arm-0'),
            self.texture,
            parent=level_block,
        )

        return level_block

    # def animate_status_update(self, can_play):
    #     self.can_play_animate = can_play

    def on_remove(self, level_block: Entity):
        # self.arm.on_remove()
        super().on_remove(level_block)

    @staticmethod
    def on_pushed(level_block: Entity):
        # self.animate_status_update(False)
        arm = level_block.arm
        arm.seq = arm.animate_position(push_phase1, duration=half_duration)[0]
        arm.seq.append(Func(arm_phase2_animate(level_block, 'piston-push-arm-1', push_phase2)))
        # self.arm.seq.append(Func(lambda: self.animate_status_update(True)))

    @staticmethod
    def on_pulled(level_block: Entity):
        # self.animate_status_update(False)
        arm = level_block.arm
        arm.seq = arm.animate_position(push_phase1, duration=half_duration)[0]
        arm.seq.append(Func(arm_phase2_animate(level_block, 'piston-push-arm-0', (0, 0, 0))))
        # arm.seq.append(Func(lambda: self.animate_status_update(True)))

    @staticmethod
    def ready_model(level_block: Entity, name):
        return level_block.arm.model_name == fetch_asset(name) \
            # and not (hasattr(self.arm, 'seq') and not level_block.arm.seq.finished) \
        # and level_block.can_play_animate

    def is_hovered(self, level_block: Entity):
        return super().is_hovered(level_block) or level_block.arm.hovered

    @staticmethod
    def toggle(level_block: Entity):
        if PistonBlock.ready_model(level_block, 'piston-push-arm-0'):
            return PistonBlock.on_pushed(level_block)

        elif PistonBlock.ready_model(level_block, 'piston-push-arm-1'):
            return PistonBlock.on_pulled(level_block)

    def debug_on_hover_press(self, level_block: Entity, key):
        if key == 'm':
            PistonBlock.toggle(level_block)

    def debug_loop_toggle(self):
        sequence = Sequence(Func(self.toggle), duration=half_duration * 2, loop=True)
        sequence.start()


class StickPistonBlock(PistonBlock):
    def __init__(self):
        super().__init__(fetch_asset('piston-stick.png'))


Block.register_block('piston', PistonBlock())
Block.register_block('stick_piston', StickPistonBlock())
