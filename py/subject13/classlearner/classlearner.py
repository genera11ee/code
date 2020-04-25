class Sword:
    weight = 0
    size = 0
    damage = 0
    name = ""
    def attack(self):
        print("The damage of " + self.name + " is " + str(self.damage))
    def defend(self, enemy_damage):
        print(self.name + " is damaged by " + str(enemy_damage) + " hitpoints")

narsil = Sword()
narsil.weight = 50
narsil.size = 40
narsil.name = "Narsil"
narsil.damage = 30

excalibur = Sword()
excalibur.weight = 60
excalibur.size = 30
excalibur.name = "Excalibur"
excalibur.damage = 40

narsil.attack()
excalibur.defend(30)
excalibur.attack()
narsil.defend(40)

