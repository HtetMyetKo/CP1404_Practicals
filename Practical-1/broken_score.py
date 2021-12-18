"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# score = float(input("Enter score: "))

import random

score = random.randint(0,100)
print(score)

if score < 0 or score > 100:
        print("Invalid score")
elif score < 50:
        print("Bad")
elif score > 50:
        print("Passable")
elif score > 90:
        print("Excellent")
