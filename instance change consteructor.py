class Student:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
s1 = Student("Kartik")
print(s1.name)

s1.change_name("Shyam")
print(s1.name)
