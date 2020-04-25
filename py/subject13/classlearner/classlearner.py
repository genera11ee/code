class Sword:
    def __init__(self, weight, size, damage, name):
        self.weight = weight
        self.size = size
        self.damage = damage
        self.name = name
    def attack(self):
        print("The damage of " + self.name + " is " + str(self.damage))
    def defend(self, enemy_damage):
        print(self.name + " is damaged by " + str(enemy_damage) + " hitpoints")

narsil = Sword(50, 40, 30, "Narsil")

excalibur = Sword(60, 30, 40, "Excalibur")

narsil.attack()
excalibur.defend(30)
excalibur.attack()
narsil.defend(40)

