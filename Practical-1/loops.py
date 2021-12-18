# a. count in 10s from 0 to 100

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1:

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars

n = int(input("Number of stars: "))
print("*" * n)

# d. print n lines of increasing stars

rows = int(input("Enter rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end=' ')
    print()