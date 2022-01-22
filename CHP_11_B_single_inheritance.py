#single interitance

class Employee:                           #this is a Parent class
    company = "Google"

    def showDetails(self):                 #this whole is copied oh the 14 line to override
        print("this is an employee")



class Programmer:                        #this is a child class
    language = 'python'
    company  = 'Youtube'

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):                  #this is called overriding where you can the things from the Employee class  
        print("this is an programmmer")

e = Employee()
e.showDetails()
p = Programmer()
p.getLanguage
print(p.language)
print(p.company)