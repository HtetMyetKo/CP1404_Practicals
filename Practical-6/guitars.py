from guitar import Guitar

def main():

    """Create a list."""
    guitars = [ Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    print("My guitars!")
    name = input("Name: ")
    while name.strip() == "":
        print("Input can not be blank")
        name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(new_guitar, "added.")


    if guitars:

        # guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_check = ""
            if guitar.is_vintage():
                vintage_check = "vintage"
            print("Guitar {0}: {1.name:>22} ({1.year}), worth ${1.cost:10,.2f}({2})".format(i + 1, guitar, vintage_check))
    else:
        print("Invalid collection.........")


main()