from entity.entity import MinecraftEntity


class Mob(MinecraftEntity):

    def __init__(self):
        super().__init__(model='player')


class PathfinderMob(Mob):
    pass
