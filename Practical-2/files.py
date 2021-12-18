# 1

out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

# 3

in_file = open("numbers.txt", "r")
first = int(in_file.readline())
second = int(in_file.readline())
sum = first + second
print("Total: ", sum)
in_file.close()

# 4

in_file = open("numbers.txt", "r")
total = 0
for i in in_file:
    number = int(i)
    total += number
print(total)
in_file.close()
