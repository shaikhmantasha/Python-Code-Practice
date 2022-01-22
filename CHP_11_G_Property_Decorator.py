class Employee:
    company = "bharat gas"
    salary = 5600
    bonus_salary = 400
    #total_salary = 5400

    @property
    def totalSalary(self):
        return self.salary + self.bonus_salary

    @totalSalary.setter
    def totalSalary(self , val):
        self.bonus_salary = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800           #this is the val
print(e.salary)
print(e.bonus_salary)
