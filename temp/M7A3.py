# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 7 Assignment 3

class User:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.user_id = 0
        self.last_login = ''
        self.password = ''

    def __init__(self, first_name, last_name, user_id, last_login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.last_login = last_login
        self.password = password

    def describe_user(self):
        print(f"Accessing user {self.user_id}:")
        print(f"{self.first_name} {self.last_name} last logged in on {self.last_login}")

    def greet_user(self):
        print(f"Welcome to the jungle {self.first_name} {self.last_name}, you gonna die")

    def new_login(self, month, day, year):
        if month > 12 or month < 1:
            print("That is not a valid month")
        elif day > 31 or day < 1:
            print("That is not a valid day")
        elif year < 1:
            print("That is not a valid year")
        else:
            month = set_month(month)
            self.last_login = f"{month} {day}, {year}"

class Admin(User):
    def __init__(self, first_name, last_name, user_id, last_login, password):
        super().__init__(first_name, last_name, user_id, last_login, password)
        self.privileges = []

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        print(f"{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")


def set_month(month_num):
    month = ""
    if month_num == 1:
        month = "January"
    elif month_num == 2:
        month = "February"
    elif month_num == 3:
        month = "March"
    elif month_num == 4:
        month = "April"
    elif month_num == 5:
        month = "May"
    elif month_num == 6:
        month = "June"
    elif month_num == 7:
        month = "July"
    elif month_num == 8:
        month = "August"
    elif month_num == 9:
        month = "September"
    elif month_num == 10:
        month = "October"
    elif month_num == 11:
        month = "November"
    elif month_num == 12:
        month = "December"
    return month


#Hard Code
jim = User(first_name='Jim',
           last_name='Bob',
           user_id=1000,
           last_login='June 12, 1998',
           password='password123')
jim.describe_user()
jim.greet_user()
joe = User('Joe',
           'Bob',
           1001,
           'July 4, 2001',
           'babygirl')
joe.greet_user()
joe.describe_user()
joe.new_login(2, 3, 2025)
joe.describe_user()
joe.new_login(15, 3, 2025)
joe.new_login(2, 35, 2025)
joe.new_login(2, 3, -55)

alice = Admin('Alice',
              'Wonder',
              1,
              'September 3, 2022',
              'P@ssw0rd')
alice.add_privilege('delete post')
alice.add_privilege('delete user')
alice.add_privilege('add user')
alice.add_privilege('give admin rights')
alice.show_privileges()