"""
CP1404/CP5632 Practical
UnreliableCarTests
"""

from unreliable_car import  UnreliableCar

def main():
    """Test some UnreliableCars."""
    # create cars with different reliabilities
    test_car = UnreliableCar("Hummer", 200, 50)
    print("{:7} drove {:2}km".format(test_car.name, test_car.drive(5)))
    print(test_car)

    good_car = UnreliableCar("Strong", 200, 90)
    bad_car = UnreliableCar("Dummy", 200, 10)

    # Simulates the distance driven and generates the results

    for i in range(1, 10):
        print("While driving {}km:".format(i))
        print("{:7} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:7} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
        print("{:7} drove {:2}km".format(test_car.name, test_car.drive(i)))

    # Print the final statistics
    print(good_car)
    print(bad_car)
    print(test_car)

main()
