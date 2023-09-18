# Class : template/blueprint of real-world entities (i.e Objects) that has properties (data members )and behaviour(member function)
# basically a user-defined datatype

# Objects : instance of class

# Name od class always starts with capital letter
class Phone :
    def make_call(self):
        print("Make call")
    def play_game(self):
        print("Playing Game")

    def set_color(self,color):
        self.color=color
    def show_color(self):
        print(self.color)

p1=Phone()

p1.make_call()
p1.play_game()
p1.set_color("red")
p1.show_color()

#################### CONSTRUCTORS #####
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def details(self):
        print("Name is ",self.name)
        print("Age is ",self.age)
        print("Salary is ",self.salary)
        print("Gender is ",self.gender)

e1=Employee('Ram',23,30000,'Male')
e1.details()
