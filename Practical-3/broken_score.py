def main():
    """Get a user's score"""
    score = float(input("Enter score: "))
    print(distinguish_grade(score))

def distinguish_grade(score):
    """Distinguish grades based on the score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score >= 50:
        print("Passable")
    elif score > 90:
        print("Excellent")

main()

"""A new part to generate a random score without user input"""
# import random
# score = random.uniform(0, 100)
# print(score)