"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    new_car = Car("Limo", 100)

    new_car.add_fuel(20)
    print("fuel =", new_car.fuel)
    print(new_car)

    new_car.drive(115)
    print("odo =", new_car.odometer)
    print(new_car)


main()