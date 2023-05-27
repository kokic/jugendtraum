from ursina import curve, Func, Sequence, mouse, Vec3

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


class PistonBlock(Block):

    def __init__(self, **kwargs):
        super().__init__(
            model=fetch_asset('piston-push-base'),
            texture=fetch_asset('piston.png'),
        )

        self.identifier = 'piston'

        self.arm = EntityBlock(
            fetch_asset('piston-push-arm-0'),
            fetch_asset('piston.png'),
        )
        self.arm.parent = self
        self.face = ViewDirection.FRONT

        self.can_play_animate = True

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        if name == 'face':
            self.rotate_by_face(value)

        super().__setattr__(name, value)

    def rotate_by_face(self, face: ViewDirection):
        if face.back():
            self.rotation_y = 180
        elif face.left():
            self.rotation_y = 90
        elif face.right():
            self.rotation_y = -90
        elif face.top():
            self.rotation_x = 90
        elif face.bottom():
            self.rotation_x = -90

    # def place(self, position):
    #     block = PistonBlock(position=position)
    #     block.face = get_face_from_normal(mouse.world_normal)
    #     return block

    def animate_status_update(self, can_play):
        self.can_play_animate = can_play

    def on_remove(self):
        self.arm.on_remove()
        super().on_remove()

    def on_pushed(self):
        self.animate_status_update(False)
        self.arm.seq = self.arm.animate_position(push_phase1, duration=half_duration)[0]
        self.arm.seq.append(Func(self.arm_phase2_animate('piston-push-arm-1', push_phase2)))
        self.arm.seq.append(Func(lambda: self.animate_status_update(True)))

    def on_pulled(self):
        self.animate_status_update(False)
        self.arm.seq = self.arm.animate_position(push_phase1, duration=half_duration)[0]
        self.arm.seq.append(Func(self.arm_phase2_animate('piston-push-arm-0', (0, 0, 0))))
        self.arm.seq.append(Func(lambda: self.animate_status_update(True)))

    def ready_model(self, name):
        return self.arm.model_name == fetch_asset(name) \
            and not (hasattr(self.arm, 'seq') and not self.arm.seq.finished) \
            and self.can_play_animate

    def arm_phase2_animate(self, model, position):
        def generator():
            self.arm.update_model(fetch_asset(model))
            self.arm.collider = 'mesh'

            self.arm.animate_position(
                value=position,
                duration=half_duration,
                curve=curve.out_expo
            )

        return generator

    def is_hovered(self):
        return self.hovered or self.arm.hovered

    def toggle(self):
        if self.ready_model('piston-push-arm-0'):
            return self.on_pushed()

        elif self.ready_model('piston-push-arm-1'):
            return self.on_pulled()

    def debug_on_hover_press(self, key):
        if key == 'm':
            self.toggle()

    def debug_loop_toggle(self):
        sequence = Sequence(Func(self.toggle), duration=half_duration * 2, loop=True)
        sequence.start()


class StickPistonBlock(PistonBlock):

    def __init__(self, **kwargs):
        super().__init__()

        self.identifier = 'stick_piston'

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.arm.texture = fetch_asset("piston-stick.png")

    def place(self, position):
        block = StickPistonBlock(position=position)
        block.face = get_face_from_normal(mouse.world_normal)
        return block
