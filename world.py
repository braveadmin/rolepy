#World definition module
import random
import enemies


class MapTile:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.ReconDroid()
            self.alive_text = "A Recon droid appears in front of you" \
                            "a little cannon appears below the crystal sphere supposed to be an eye!"
            self.dead_text = "An amount of metal junk that once was a recon droid." \
                            " Still emits a lighty buzz."
        elif r < 0.80:
            self.enemy = enemies.SpacePirate()
            self.alive_text = "A space pirate  appears in front of you" \
                                "he activates his shock stick!"
            self.dead_text = "The corpse of the dead space pirate." \
                            "The cybernetic implants still sparks."
        else:
            self.enemy = enemies.SentinelDroid()
            self.alive_text = "A sentinel droid appears in front of you" \
                            "some beeps indicates he is ready for the combat."
            self.dead_text = "the intimidating sentinel droid rests in the floor."

        #super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp -= self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with flickering torch on the wallself.
        You can make out four paths, each equally as dark and foreboding.
        """

class BoringTile(MapTile):
    def intro_text(self):
        return """
        Nothing interesting here.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        you see a bright light in the distance...
        ... it grows as you get closer! It's Sunlight!


        Victory is yours!
        """

world_map = [
    [None,VictoryTile(1,0),None],
    [None,EnemyTile(1,1),None],
    [EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
    [None,EnemyTile(1,3),None]
]

#Locates a tile at a coordinate
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
