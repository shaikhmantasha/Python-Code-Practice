
class Person:
    country = "India"

    def __init__(self):
        print("Initizing person...\n")

    def takeBreath(self):
        print("I am breathing...")



class Employee(Person):
    company = "Google"

    def __init__(self):
        super().__init__()                   #if we comment out the super()__init__ only the print on 18 line will be print and the parent one is not calles
        print("initializing Emplyeee...\n")
    
    def getSalary(self):
        print(f"salary is {self.Salary}")

    def takeBreath(self):
        print("the Employee is breathing.....")



class Programmer(Employee):
    company = "fever"

    def __init__(self):
        super().__init__()               
        print("Initialzing Programmer...\n")

    def getSalary(self):
        super().takeBreath()              #this will first print the parent takeBreath and then will print his own takeBreath
        print("no salary for programmers")

    def takeBreath(self):
        print("i am a programmer and i am breathing ++++")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()
