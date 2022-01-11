"""
CP1404/CP5632
Taxi simulator
"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():

    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)

    menu_choice = input(">>> ").lower()
    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)

            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                taxi_fare = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, taxi_fare))
                total_bill += taxi_fare
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

def run_tests():
    """Run tests to show workings of Car and Taxi classes."""

    tesla = Car("Tesla", 200)
    tesla.drive(30)
    print("{}, fuel={}, odometer={}".format(tesla.name, tesla.fuel, tesla.odometer))

    prius = Taxi("Prius 1", 100)
    prius.drive(25)
    print(prius, prius.get_fare())
    prius.start_fare()
    prius.drive(40)
    print(prius, prius.get_fare())

    limo = SilverServiceTaxi("Limo", 100, 2)
    print(limo, limo.get_fare())
    limo.drive(10)
    print(limo, limo.get_fare())

    hummer = SilverServiceTaxi("Limo", 200, 4)
    print(hummer, hummer.get_fare())
    hummer.drive(10)
    print(hummer, hummer.get_fare())


main()
