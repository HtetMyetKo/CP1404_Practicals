"""
CP1404/CP5632 UnreliableCar class
"""

import random
from car import Car

class UnreliableCar(Car):
    """UnreliableCar class derived from Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar  based on parent class Car."""

        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car with random reliability."""
        random_number = random.uniform(1, 100)  # Generates a random float
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance) # Signature
        return distance_driven