class Employee:
    company = "Google"
    def getsalary(self , sign):
        print(f"The salary is for the employee working in {self.company} is {self.salary} \n {sign}")


#sometime we need a funtion that doesnt use the self parameter we can define a static method like this

    @staticmethod
    def greet():
        print("Good Morning user, ")

    @staticmethod
    def time():
        print("The time is 9AM int he morning")

harry = Employee()
harry.salary = 10000
harry.getsalary("thanks!")       #Emoployee.getsalary(harry) 
harry.greet()    #Employee.greet
harry.time()