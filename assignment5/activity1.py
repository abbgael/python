# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I have the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass: FlyingHero (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        # Polymorphism: this overrides the base method
        print(f"{self.name} takes off and flies at {self.flight_speed} km/h using {self.power}!")

# Subclass: TechHero (inherits from Superhero)
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def use_power(self):
        print(f"{self.name} activates gadgets: {', '.join(self.gadgets)} powered by {self.power}!")
