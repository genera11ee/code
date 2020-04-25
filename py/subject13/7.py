class Cat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def sleep(self):
        print(self.name + " is sleeping")

tom = Cat("Tom", "Tabby")
tom.sleep()