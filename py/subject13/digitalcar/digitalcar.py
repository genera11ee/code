class Car:
    def __init__(self, name, speed, weight, color):
        self.name = name
        self.speed = speed
        self.weight = weight
        self.color = color
    def drive(self):
        print(self.name + " is driving at " + str(self.speed) + " km/h.")
    
    def weight_check(self, person_weight):
        if person_weight > self.weight:
            print("You are too heavy for this car")
        else:
            print("Your weight is acceptable for this car")

    def color_check(self):
        print(self.name + "'s car color is " + self.color)
    

jack = Car("Jack", 200, 150, "Black")
gracie = Car("Gracie", 180, 120, "Red")
jack.drive()
gracie.drive()
jack.weight_check(60)
gracie.weight_check(200)
jack.color_check()
gracie.color_check()
