class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(self.name, self.gender, self.age)

class Student(Person):
    def __init__(self, name, gender, age):
        Person.__init__(self, name, gender, age)
        self.branch= branch

    def show(self):
        print(self.branch)

s= Student('Soham', 'M', 21, 'IT')
super.display()
Student.show()
