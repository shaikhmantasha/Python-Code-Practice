class Number:
    def __init__(self , num):
        self.num = num

    def __add__(self , num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self , num3):
        print("lets multipley")
        return self.num * num3.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 
mul = n1 * n2
print(sum)
print(mul)

#__sub__ these are all dunder methods 
# for add(+)       __add__ method is used
# for subtract(-)  __sub__ method is used
# for multiple(*)  __mul__ method is used
# for divide(/)    __truediv__ method is used
# for add(//)      __floordiv__ method is used


#for more methods go to (pyhton docs for opperator overloading)