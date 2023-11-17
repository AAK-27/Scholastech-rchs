class Vehicle():
    def __init__(self, name, numWheels, color):
        self.name = name
        self.numWheels = numWheels
        self.color = color

    def __str__(self):
        return self.color + " " + self.name + " with " + str(self.numWheels) + " wheels"
    
train = Vehicle("train", 8, "blue")
print(train)

class Car(Vehicle):
    def __init__(self, name, color, miles):
        Vehicle.__init__(self, name, 4, color)
        self.miles = miles

car1 = Car("Ferrari", "red", 1000)
print(car1)