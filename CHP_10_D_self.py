class Employee:
    company = "Google"
    def getsalary(self):            #def is a fucntion and self is a parameter
        print(f"The salary is for the employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getsalary()       #Emoployee.getsalary(harry) 