from guitar import Guitar

def guitar_test():
    
    """Set values"""

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar Guitar", 2013, 2222.22)

    print(f"{guitar.name} get_age() - Expected {98}. Got {guitar.get_age()}")

    print(f"{another_guitar.name} get_age() - Expected {7}. Got {another_guitar.get_age()}")

    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")

    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")

if __name__ == '__main__':
    guitar_test()