class Cat:
    name = ""
    species = ""
    weight = 0
    color = ""

tom = Cat()
tom.name = "Tom"
tom.species = "Tabby"
tom.weight = 2
tom.color = "Orange"

athena = Cat()
athena.name = "Athena"
athena.species = "Siamese"
athena.weight = 1.5
athena.color = "Brown"

print("Athena is a " + athena.species + " cat.")
print("But Tom is a " + tom.species + " cat.")