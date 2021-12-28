"""Declares constants"""

CURRENT_YEAR = 2020
VINTAGE_AGE = 50

class Guitar:
    """Creates a guitar class ."""
    def __init__(self, name="", year=0, cost=0):
        """Initiates a guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Gets the guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks whether the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year