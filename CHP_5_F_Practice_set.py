# #PROBLEM NO 1
# lang = { "baal" : "hairs" ,
# "kapde" : "clothes",
# "chappal" : "shoes",
# "kalaa" : "black"
# }
# print("options are :" , lang.keys())
# a = input("enter your hindi word\n")

# # print("your hindi word is :" ,lang[a])

# #below line will not th=hrow an error is the key is not present int he dictionary
# print("your hindi word is :" ,lang.get(a))

#PROBLEM NO 2

# num1 = int(input("enter your numbe 1"))
# num2 = int(input("enter your numbe 2"))
# num3 = int(input("enter your numbe 3"))
# num4 = int(input("enter your numbe 4"))
# num5 = int(input("enter your numbe 5"))
# num6 = int(input("enter your numbe 6"))
# num7 = int(input("enter your numbe 7"))
# num8 = int(input("enter your numbe 8"))

# s = {num1, num2, num3, num4, num5 ,num6 ,num7 ,num8}
# print(s)

#PROBLEM NO 3
# s = {"18" , 18,12.0}         #this will be printed as both of them have a unique value
# print(s) 

#PROBLEM NO 4
# s ={20, 20.0, "45"}
# print(s)
# print(len(s))

#PROBLEM NO 5

favLang={}
a = input("enter your favorite language shubham:\n")
b = input("enter your favorite language ankit:\n")
c = input("enter your favorite language rahul:\n")
d = input("enter your favorite language mushi:\n")

favLang ['shubham'] = a
favLang ['ankit'] = b
favLang ['rahul'] = c
favLang ['mushi'] = d

print(favLang)

