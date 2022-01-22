#-------------------------------------QUESTION NO .1-------------------------------------------------------------------------
# find out the gretest of numbers

def maximum(num1 , num2 , num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:  
            return num3
    else:
        if (num2 > num3): 
            return num2
        else:
            return num3

m = maximum(45,987,89)
print("the biggest number is " + str(m))


#-------------------------------------QUESTION NO .2-------------------------------------------------------------------------
def farh(cel):
  return(cel * (9/5)) + 32
c = 78
f=farh(c)
print("fahreinheight ttempreture is : "+str(f))


#-------------------------------------QUESTION NO .3-------------------------------------------------------------------------
print("hello" , end=" ")
print("how", end=" ")
print("are", end=" ")
print("you",)


#-------------------------------------QUESTION NO .4-------------------------------------------------------------------------

def sum_recurssive(n):
    if n == 1 or n == 0:
        return 1
    return n  + sum_recurssive (n-1)

f = sum_recurssive(4)
print(f)


#-------------------------------------QUESTION NO .5-------------------------------------------------------------------------

n = 3
for i in range (n):
    print("*" * (n-i))


#-------------------------------------QUESTION NO .6-------------------------------------------------------------------------
# done by myself

l=5
def inch(cm):
    return (l*2.54)
j= inch(l)
print(j)

#-------------------------------------QUESTION NO .6-------------------------------------------------------------------------

name = "          muskan is beautiful             "
print(name)
print(name.strip())                                 #the fucntion strip removes extra space 


#-------------------------------------QUESTION NO .7-------------------------------------------------------------------------

def remove_and_split(string , word):
    new = string.replace(word , "")        # here we have replaced word with ""(blank)
    return new.strip() 

name = "     harry iss good      "
n = remove_and_split(name , "harry")
print(n)


#-------------------------------------QUESTION NO .8-------------------------------------------------------------------------
#home work

a = 5
for i in range (1 , 11):
    print("5" , "X" , i ,"=" , a*i)

