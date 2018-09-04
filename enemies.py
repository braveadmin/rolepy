#enemies definition

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class ReconDroid(Enemy):
    def __init__(self):
        self.name = "Recon Droid"
        self.hp = 5
        self.damage = 2

class SpacePirate(Enemy):
    def __init__(self):
        self.name = "Space Pirate"
        self.hp = 10
        self.damage = 5

class SentinelDroid(Enemy):
    def __init__(self):
        self.name = "sentinel Droid"
        self.hp = 15
        self.damage = 7
