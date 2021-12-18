try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("It can cause ZeroDivisionError")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. ValueError occurs when the input is not a number (an integer).

#2. ZeroDivisionError occurs when the denominator is 0.

#3.    while denominator == 0:
#         print("It can cause ZeroDivisionError")
#         denominator = int(input("Enter the denominator: "))

