# # to slice the words into pieces 
 
#   # SHAIKH
#   # 012345

# name = "shaikh"
# print(name[2])
# print(name[0:3])  # this will print letters from 0 to 2 and the 3 letter will be excluded
# print(name[:5] )   # this is same as [0:5]
# print(name[1: ])  # this will print the number from 1 till the last number


# # NEGATIVE INDICES ARE USED WHEN THERE ARE TOO MANY LETTER AND YOU WANT TO KNOW THE NUMBER OF THE LAST LETTER

#   #SHAIKHMANTASHSOHR       A  B  A  L  I
#                         # -5 -4 -3 -2 -1 

# c = name[:-1]        #this is showing for the above name = shaikh
# print(c)


# slicing with skip value

name = "harryisgood"
# d = name[0::2]   # will write every second word
d = name[0::3]   # will print every third word
print(d)



