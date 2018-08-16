#enemies definition

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Slime(Enemy):
    def __init__(self):
        super().__init__(name="Slime", hp=10, damage=2)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=15, damage=5)
