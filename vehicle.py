# Base Class
class Vehicle:
    def move(self):
        print("The vehicle moves")

# Derived Classes
class Car(Vehicle):
    def move(self):
        print("🚗 The car drives on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane flies in the sky")

class Boat(Vehicle):
    def move(self):
        print("🚢 The boat sails in the water")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
