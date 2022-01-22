


#if they have their own method they will use that otherwise they are going to use the one which is inheritered by their parent or child
class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Google"

    def getSalary(self):
        
        print(f"salary is {self.Salary}")

    def takeBreath(self):
        print("the Employee is breathing.....")

class Programmer(Employee):
    company = "fever"

    def getSalary(self):
        print("no salary for programmers")

    # def takeBreath(self):
    #     print("i am a programmer and i am breathing ++++")

p = Person()
p.takeBreath()
#print(p.company)     #throws an error   

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
