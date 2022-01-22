class Employee:                 #parent
    company = "Visa"
    eCode = 120

class Freelancer:                #parent
    company = "Fiverrr"
    level = 0

    def upgradeLevel(self):      
        self.level = self.level + 1 

class Programmer(Employee , Freelancer):      #child that hass all the qoalities of parent
    name = "muskan"

p = Programmer()
p.upgradeLevel()

print(p.level)
print(p.company)           #this willl print visa as visa is written first in line 12 in ()

