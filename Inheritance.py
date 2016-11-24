

class Character(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def printName(self):
        print(self.name)


class NPC(Character):

    def __init__(self, name, health):
        self.status = "Non-Playable Character"
        super(NPC, self).__init__(name, health)


class Enemy(NPC):

    def __init__(self, name, health, damage):
        super(Enemy, self).__init__(name, health)
        self.damage = damage

    def get_dmg(self):
        print(self.damage)


class Goblin(Enemy):

    def __init__(self, name, health, damage):
        super(Goblin, self).__init__(name, health, damage)

    def smash(self):
        print("Goblin used Smash and took %s damage!" % self.damage)


class Friendly(NPC):

    def __init__(self, name, health):
        super(Friendly, self).__init__(name, health)


class PC(Character):

    def __init__(self, name, health):
        self.status = "Playable Character"
        super().__init__(name, health)


class Archer(PC):

    def __init__(self, weapon, name, health):
        super().__init__(name, health)
        self.weapon = weapon


class Weapon(object):

    def __init__(self, dmg, weight):
        self.dmg = dmg
        self.weight = weight


class Mace(Weapon):

    def __init__(self, dmg, weight):
        super().__init__(dmg, weight)

    def bonus(self):
        self.dmg = self.dmg*2

a = Archer("Longbow", "Kennedy", 100)
e = Enemy("Goblin", 50, 100)

g = Goblin("Goblin", 50, 300)


"""print(a.printName())
print(e.get_dmg())"""

print(g.smash())
