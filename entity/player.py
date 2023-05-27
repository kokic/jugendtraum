from ursina import curve, Func, Vec3
from ursina.prefabs.first_person_controller import FirstPersonController

from entity.carried import CarriedItem

# player hand-carried model:
# - empty (hand model)
# - item (dropping model)
# - block (block model)
#
# carried_position = Vec3(0.85, -0.55, 1)
# carried_rotation = Vec3(0, 45, 0)
# carried_origin = (0, -0.5, 0)


class Player(FirstPersonController):

    def __init__(self):
        super().__init__()

        self.carried = CarriedItem()

    # def carried_input(self, key):
    #
    #     rotation = self.carried.animate_rotation(
    #         value=carried_rotation - Vec3(0, -15, 60),
    #         duration=0.05,
    #         curve=curve.linear
    #     )[1]
    #
    #     rotation.append(Func(lambda: self.carried.animate_rotation(
    #         value=carried_rotation,
    #         duration=0.05,
    #         curve=curve.linear
    #     )))

        # if key == 'left mouse down':
        #     rotation = self.carried.animate_rotation(
        #         value=carried_rotation - Vec3(0, -30, 120),
        #         duration=0.15,
        #         curve=curve.in_out_circ
        #     )[1]
        #
        #     rotation.append(Func(lambda: self.carried.animate_rotation(
        #         value=carried_rotation,
        #         duration=0.15,
        #         curve=curve.in_out_circ
        #     )))

            # position = self.carried.animate_position(
            #     value=carried_position - Vec3(2.5, 0, -2),
            #     duration=0.15,
            #     curve=curve.linear
            # )[0]
            #
            # position.append(Func(lambda: self.carried.animate_position(
            #     value=carried_position,
            #     duration=0.15,
            #     curve=curve.linear
            # )))

        # if key == 'right mouse down':


# (0, -15, 0)
