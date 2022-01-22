# # #-----------------------------------------------QUESTION NO 1------------------------------------------------------------------------------------
# # #QUESTION = Create a class C2d vector and use it to create anotther class representing C3d vector

# # from _typeshed import Self


# # class C2dvec:
# #     def __init__(self , i , j):
# #         self.icap = i
# #         self.jcap = j

# #     def __str__(self):
# #         return f"{self.icap}i + {self.jcap}j"

# # class C3dvec(C2dvec):
# #     def __init__(self , i , j , k):
# #         super().__init__(i , j)
# #         self.kcap = k

# #     def __str__(self):
# #         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# # vector2d = C2dvec(1 , 3)
# # vector3d = C3dvec(2 , 6 , 9)
# # print(vector2d)
# # print(vector3d)

# # #-----------------------------------------------QUESTION NO 2------------------------------------------------------------------------------------
# # #multi levele inheritance

# # class Animals:
# #     pass

# # class Pets(Animals):
# #     pass

# # class Dogs(Pets):

# #     @staticmethod
# #     def bark():
# #         print("bhow bhow!")

# # d = Dogs()
# # d.bark()

# #-----------------------------------------------QUESTION NO 3------------------------------------------------------------------------------------
# # [FORMULA] salaryAfterIncrement = salary * increment
# #so if we have to fine increment it will be --- increment = salaryAfterIncrement/salary


# # class Employee:
# #     salary = 1000 
# #     increment = 1.5
    
# #     @property
# #     def salaryAfterIncrement(self): 
# #         return self.salary * self.increment

# #     @salaryAfterIncrement.setter
# #     def salaryAfterIncrement(Self , sai):       #sai is salaryAfterIncrement      #showing error of self i odnt know what it is
# #         self.increment = sai /self.salary

# # e = Employee()
# # print(e.salaryAfterIncrement)
# # print(e.increment)
# # e.salaryAfterIncrement = 2000
# # print(e.increment)


# #-----------------------------------------------QUESTION NO 4------------------------------------------------------------------------------------
# # quciker way to fiind complex number
# #FORMULA = (a + bi) where a = real numebr and i = imaginary 



# # class Complex:
# #     def __init__(self , r, i ):              #  r- real , i-imaginary
# #         self.real = r
# #         self.imaginary = i

# #     def __add__(self, c):                    #  c - complex number
# #         return complex(self.real + c.real , self.imaginary + c.imaginary)

# #     def __str__(self):
# #         return f"{self.real} + {self.imaginary}i"

# # c1= complex(1 , 8)
# # c2 = complex(2 , 9)
# # print(c1 + c2)



# #-----------------------------------------------QUESTION NO 5------------------------------------------------------------------------------------
# #   [ FROMULA =  (a+bi)(c+di) = (ac−bd) + (ad+bc)i ]
# #FOR MULTIPLYING COMPLEX NUMEBRS

# # (ac−bd) + (ad+bc)i              {this part is used in the __mul__ operator}


# class Complex:
#     def __init__(self , r, i ):              #  r- real , i-imaginary
#         self.real = r
#         self.imaginary = i

#     def __mul__(self , c):
#         mulReal = self.real * c.real  -  self.imaginary*c.imaginary
#         mulImaginary = self.real * c.imaginary   +   self.imaginary * c.real
#         return(mulReal , mulImaginary)

#     def __str__(self):
#         if self.imaginary<0:
#             return  f" {self.real}  -  {-self.imaginary}i " 
#         else:
#             return f" {self.real}  +  {self.imaginary}i "     #if there is - signs in self.imaginary and we cant it to show then we can add one condition

# c1= complex(1 , -4)
# c2 = complex(331 , -37)
# print( c1  *  c2 )



#-----------------------------------------------QUESTION NO 6------------------------------------------------------------------------------------

# #stupid o
# class Vector:
#     def __init__(self , vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a {index} +" 
#             index += 1
#         return str1[:-1] 

#     def __add__(self , vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] +  vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self , vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] *  vec2.vec[i]          
#         return sum

# v1 = Vector([1 , 4 , 6])             #1*1 = 1 ,4*6=24+1 = 25 , 6*9=54 +25 =79
# v2 = Vector([1 ,6, 9 ])
# print(v1+v2)
# print(v1*v2)



#-----------------------------------------------QUESTION NO 7------------------------------------------------------------------------------------
# 3 dimension ( i j k )

# class Vector:
#     def __init__(self , vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"


# v1 = Vector([1 , 4 , 6])          
# v2 = Vector([1 ,6, 9 ])
# print(v1)
# print(v2)



#-----------------------------------------------QUESTION NO 6------------------------------------------------------------------------------------


class Vector:
    def __init__(self , vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a {index} +" 
            index += 1
        return str1[:-1] 

    def __add__(self , vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] +  vec2.vec[i])
        return Vector(newList)

    def __mul__(self , vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] *  vec2.vec[i]          
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1 , 4 , 6 , 4])           
v2 = Vector([1 ,6, 9 ])
# print(v1+v2)
# print(v1*v2)
print(len(v1))
print(len(v2))


#-----------------------------------------------QUESTION NO ------------------------------------------------------------------------------------

