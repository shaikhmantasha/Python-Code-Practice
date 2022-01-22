class Employee:
    company = "Camel"
    salary = 100
    location = "Mumbai"

#  def changeSalary(self , sal):                 # this will directly call the class method without using instance methotd
        # self.__class__.salary = sal
    
    @classmethod
    def changeSalary(cls , sal):
        cls.salary = sal

    

e = Employee()
print(e.salary)
e.changeSalary(452)
print(e.salary)
print(Employee.salary)