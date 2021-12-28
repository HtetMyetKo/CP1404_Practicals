
class student:

    def __init__(self, first_name="", last_name="", id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.credit = 0

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id}) has {self.credit} credits"

if __name__ == '__main__':
    s1 = student("Red", "Ket", 12)
    print(s1)

    s2 = student(first_name= "Gary")
    print(s2)

    s3 = student(first_name= "Gold", id= 14)
    print(s3)