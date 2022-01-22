##PROBLEM NO 1
# num1 = int(input("enter your number  1 :"))
# num2 = int(input("enter your number  2 :"))
# num3 = int(input("enter your number  3 :"))
# num4 = int(input("enter your number  4 :"))

# if(num1 > num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 =num2
# else:
#     f2=num3

# if(f1>f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2)  + " is greatest")

#problem no 2

# sub1 = int(input("enter marks of first subject"))
# sub2 = int(input("enter marks of second subject"))
# sub3 = int(input("enter marks of third subject"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are failed because you have failed in one subject")

# elif(sub1+sub2+sub3)/3 <40:
#     print("you have failed because you have less then 40")

# else:
#     print("you have passed")

#####   problem no 3

# text =input("enter the text\n")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("this is a spam")
# else:
#     print("this is not a spam")

####     problem no 4

# name = input("Enter your name\n")
# if(len(name)<10):
#     print("name has character less then 10")
# else:
#     print("your name has more then 10 character")

###      practice no 5

# names = ["shruti" , "muskan" , "mantasha" , "akaab" , "ashab"]
# name = input("write your name here\n")

# if name in names:
#     print("your name is present in the list ")
# else:
#     print("your name is not present")


# marks = int(input("Enter your marks\n"))
# if marks>=90:
#     grade = "EXCELLENT"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# else:
#     grade = "FAIL"

# print("your grade is :" + grade)

post = input("write your post here\n")

if ("harry" in post ):
    print("the name harry is present")

else:
   print("harry is not present")