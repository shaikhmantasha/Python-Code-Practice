class Employee:
    company = "Google"

    def __init__(self , name , salary , subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Emplyee is created!")

    def getDetail(self):
        
        print(f"The name of the Emplyee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


muskan = Employee("muskan" ,100 , "Youtube")  
muskan.getDetail()

#muskan = Employee()   #Throws an error\

# wecanassignanything =  '''callthecalss''' Employee 