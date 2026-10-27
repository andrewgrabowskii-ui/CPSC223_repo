class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 10

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def bark(self):
        print(f"{self.name} says woof")

    def junk_test():
        print(f"This is a test")


class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)



fido = Bulldog("Fido", 37)
fluffy = Dog("Fluffy", 13)
print(fido)
print(fluffy)
fido.bark()
fluffy.bark()
Dog.junk_test()
fido.weight = 50
fido.bark()
print(f"{fido.name} weighs {fido.weight}lbs")