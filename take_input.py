'''
t = 4          
2 4 5 9  

t = 4           
2 4 11 12
'''
a, b = (int(input()),input().split())
c, d = (int(input()),input().split())

# n =int(input())
# n1 = set(map(int , input().split())
# m  = int(input())
# m1 = set(map(int , input().split())




'''
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

# '''
# from collections import namedtuple
# n = int(input())
# data = namedtuple('data' , input().split())
# s = 0
# for i in range (n):
#    s +=  int(data(*input().split()).MARKS)
# print(s / n)


import re
n = int(input())
print(n)
for i in range (n):
    num = input()
    numbersInTheString = re.findall(r"(?:^|\b)([7-9]+)(?:\b)",num)
    print(numbersInTheString)