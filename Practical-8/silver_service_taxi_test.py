"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi (Hummer) ."""
    service_taxi = SilverServiceTaxi("Hummer", 200, 4)
    service_taxi.drive(18)
    print(service_taxi)
    print(service_taxi.get_fare())

main()