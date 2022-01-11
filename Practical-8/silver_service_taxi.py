"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi under Taxi class (which is under Car class)."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi class."""
        super().__init__(name, fuel)  # Given attributes
        self.fanciness = fanciness
        self.price_per_km *= fanciness

