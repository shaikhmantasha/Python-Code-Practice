
##------------------------------------PROBLEM NO 1-----------



# table = int(input("enter the number"))
# for i in range(1 , 11):
#     # print(str(table) + str(" X ") + str(i) + "= " + str(table*i) )  #another way to write this is usinf F string

#     print(f"{table}X{i}={table*i}")

#-------------------------------------PROBLEM NO 2------------




# l1 = ['harry' , 'sohan' , 'sachin' , 'rahul']
# for name in l1:
#     if name.startswith("s"):
#        print("Hello" + name)

#-------------------------------------PROBLEM NO 3------------
# 
# 
# 
#  (done by me as HW)

# num = int(input("enter your number"))
# i = 0
# while i<=10:
#     i = i+1
#     print(f"{num}X{i}={num*i}")

#-------------------------------------PROBLEM NO 4------------



#HOW TO FIND WHETHER THE NUMBER IS PRIME OR NOT

# num = int(input("enter your number"))
# prime = True                     #this is a default value
# for i in range(2 , num):
#     if (num%i == 0):
#        prime = False
#        break
#     if prime:
#         print("this number is prime")
    
# else:
#     print("this is not a prime number")


#----------------------------------PROBLEM NO 5 ------------



#could be wrong
# num = int(input("enter natural numbers : "))
# i = 1
# while i >= 0:
#     print("the sum of first n natural numbers are :" + str(num+i))
#     break

#---------------------------------PROBLEM NO 6 ------------





#what is factoriral?
# n! = 1 x 2 x 3 x 4 x 5 x 6 x 7 .......x n
# 5! = 1 x 2 x 3 x 4 x 5

# num = int(input("enter the number :"))
# factorial = 1
# for i in range(1 , num+1):
#     factorial = factorial * i
#     print(f"the factorial of  {num} is {factorial}")

#---------------------------------PROBLEM NO 7 ------------




# yeh wala nahi samjha meko
# n =3
# for i in range(3):
#     print(" " * (n-i-1) , end="")
#     print("*" * (2*i+1) , end ="")
#     print(" " * (n-i-1))


    
#---------------------------------PROBLEM NO 8 ------------



# n = 4
# for i in range(4):        #for i in range (5)
#     print("*" * (i+1))    #print("*" + i)


#---------------------------------PROBLEM NO 9 ------------




num=int(input("enter the number :"))

for i in range(0,11):
    i=11-(i+1)
    if i == 0:
        continue
    print(f"{num} X {i}= {num*i} ")