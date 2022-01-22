# n! = 1 * 2 * 3 * 4 *....*n!

n=5
product = 1
for i in range(n):          #for i in range here: <here i starts with 0 so to make it start from 1 we have to make (i +1)
    product = product * (i+1)
print(product)


#-----------------another way of write this using funtion------------------------------------------------------------------

def factorial_iter(n):
    product = 1
    for i in range(n):
         product = product * (i+1)
    return product

f =(factorial_iter(4))
print(f)

# recurssion - is used when we have to use direct formula
# n! = 1 * 2 * 3 * 4 *....(n-1)!
# n! = n * (n-1)!

def factorial_recurssive(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial_recurssive (n-1)

f = factorial_recurssive(4)
print(f)