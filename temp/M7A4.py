# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 7 Assignment 4

class NumCouple:
    def __init__(self):
        num1 = 0
        num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def minimum(self):
        if self.num1 < self.num2:
            return self.num1
        else:
            return self.num2
    def maximum(self):
        if self.num1 > self.num2:
            return self.num1
        else:
            return self.num2
    def product(self):
        return self.num1 * self.num2

class NumThruple(NumCouple):
    def __init__(self, num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3

    def minimum(self):
        couple_min = super().minimum()
        if couple_min < self.num3:
            return couple_min
        else:
            return self.num3
    def maximum(self):
        couple_max = super().maximum()
        if couple_max > self.num3:
            return couple_max
        else:
            return self.num3
    def product(self):
        couple_prod = super().product()
        return couple_prod * self.num3

# hard-coded lines
couple = NumCouple(4, 7)
print(f"The couples minimum is {couple.minimum()}")
print(f"The couples maximum is {couple.maximum()}")
print(f"The couples product is {couple.product()}")
thruple = NumThruple(3, 5, 2)
print(f"The thruples minimum is {thruple.minimum()}")
print(f"The thruples maximum is {thruple.maximum()}")
print(f"The thruples product is {thruple.product()}")