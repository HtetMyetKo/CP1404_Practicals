"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi under Taxi class (which is under Car class)."""
    flagfall = 4.50  # 2

    def __init__(self, name, fuel, fanciness):  # 1
        """Initialise a SilverServiceTaxi class."""
        super().__init__(name, fuel)  # Given attributes
        self.fanciness = fanciness
        self.price_per_km *= fanciness


    def calculate_fare(self):  # 3
        """Get the current fare."""
        return self.flagfall + super().get_fare() # Adds flagfall value to the method from 'taxi'


    def __str__(self):  # 4
        """Return a string representation of a SilverServiceTaxi class."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
