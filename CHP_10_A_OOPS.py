'''
class is a form 
and object is the form filled called 

PascalCase
EmployeName --> pascal case

camelCase
isNumeric  -->camelcase         #only the first letter is small rest all the character are capital 
'''

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

myApplication = RailwayForm()
myApplication.name = "shaikh muskan"
myApplication.train = "rajdhani express"
myApplication.printData() 


#another example to understand OOPS concenpt is using game


class Remote():
    pass
class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

player1 = Player()
remote1 = Remote()
if(remote1.isleftpressed()):
    player1.moveLeft()