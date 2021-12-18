is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        print("THe result is: ", result)
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)