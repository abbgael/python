class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying through the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing across the water.")

