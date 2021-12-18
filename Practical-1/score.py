"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

        """Get a user's score"""

        random_score()
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



"""A function to generate a random score without user input"""

def random_score():
        import random
        score = random.uniform(0, 100)
        return score

main()