class Cat:
    name = ""
    species = ""
    def sleep(self):
        print(self.name + " is sleeping")
    def show(self):
        print(self.species + " is the species of " + self.name)
    def eat(self, food):
        print(self.name + " is eating " + food)

tom = Cat()
tom.name = "Tom"
tom.species = "Tabby"
tom.sleep()
tom.show()
tom.eat("a mouse")
# bob = Cat()
# bob.name = "Bob"
# bob.species = "Siamese"
# bob.sleep()
# bob.show()