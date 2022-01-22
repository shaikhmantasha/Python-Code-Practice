# # #------------------------------------------------QUESTION NO 1--------------------------------------------------------------------------------


# # from os import stat


# # class Programmer:
# #     company = "microsoft"

# #     def __init__(self , name , product):
# #         self.name = name
# #         self.product = product

# #     def getInfo(self):
# #         print(f"the name of the {self.company} programmer is {self.name} and the product is {self.product}")

# # muskan = Programmer("shaikh muskan" , "facebook")
# # aqsa = Programmer("shaikh aqsa" , "skype")

# # muskan.getInfo()
# # aqsa.getInfo()



# # #------------------------------------------------QUESTION NO 2--------------------------------------------------------------------------------


# # class Calculator:
# #     def __init__(self , num):
# #         self.number = num

# #     def square(self):
# #         print(f"the square of the {self.number} is {self.number **2}")

# #     def squareroot(self):
# #          print(f"the squareroot of the {self.number} is {self.number ** 0.5}")


# #     def cube(self):
# #          print(f"the cube of the {self.number} is {self.number **3}")


# # a = Calculator(3)
# # a.square()
# # a.squareroot()
# # a.cube()


# # #------------------------------------------------QUESTION NO 3--------------------------------------------------------------------------------

# # class Sample:
# #     a = "muskan"

# # name = Sample()
# # name.a = "aqsa"

# # #this will change the class attribute
# # Sample.a = "vickey"

# # print(Sample.a)
# # print(name.a)


# # #------------------------------------------------QUESTION NO 4--------------------------------------------------------------------------------


# # class Calculator:
# #     def __init__(self , num):
# #         self.number = num

# #     def square(self):
# #         print(f"the square of the {self.number} is {self.number **2}")

# #     def squareroot(self):
# #          print(f"the squareroot of the {self.number} is {self.number ** 0.5}")


# #     def cube(self):
# #          print(f"the cube of the {self.number} is {self.number **3}")


# #     @staticmethod
# #     def greet():
# #         print("********Welcome to the best calculator of the world********")

# # a = Calculator(3)
# # a.greet()
# # a.square()
# # a.squareroot()
# # a.cube()


# # #------------------------------------------------QUESTION NO 5--------------------------------------------------------------------------------

# class Train:
#     def __init__(self , name , fare , seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getInfo(self):
#         print(f"the name of the train is {self.name}")
#         print(f"the seats available are {self.seats}")

#     def fareInfo(self):
#         print(f"the fare of the train is {self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"Congragulation your ticket hass been booked, Your seat number is {self.seats}") 
#             self.seats = self.seats - 1
#         else:
#             print("sorry the train is Full")

# travel = Train("Raj Dhani Express 12133" , 60 , 2)
# travel.getInfo()
# travel.fareInfo()
# travel.bookTicket()
# travel.bookTicket()
# travel.bookTicket()


# #------------------------------------------------QUESTION NO 6--------------------------------------------------------------------------------
#can we write any other name in place of self?



class Name:
    def __init__(self ,name):
        self.name = name

    def __init__(mussu ,name , place):
       
        mussu.name = name
        mussu.place = place

book = Name("harry" , "mumbai")
print(book.name)
print(book.name)
print(book.place)
