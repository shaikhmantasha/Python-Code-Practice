

# # for i in range(int(input())):
# #         name = input()
# #         score = float(input())

# # # score_list.append([name , score])
# # # second_highest = sorted(set([score for name , score in score_list]))[1]
# # # print('\n'.join(sorted([name for name , score in score_list if score == second_highest])))


# # score_list.append([name , score])
# # set = sorted(set(score_list))[-2][-1]
# # for item in set:
# #     print(name , set)
# #     3

# # if __name__ == '__main__':
#     # n = 1
#     # score = []
#     # list  = []




# # score_list = score.append(score)
# # nested_marks = sorted(set(score))
# # print(nested_marks)
# # print (nested_marks[-2])
# # print(nested_marks[-1])

# #     for i in range(int(input())):
# #         name = input()
# #         score = float(input())

# # nested_list = []
# # nested_list.append(score)
# # for item in nested_list:
# #         sorted(set(nested_list()))
# #         print(item(name)[-2][-1])






# for _ in range(int(input())):
#     name = input()
#     score = float(input())
    
# lst=[['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
# names=[]

# lowest = lst[0].__getitem__(1)
# second_lowest=0
# for l in lst:
#     if l[1] < lowest:
#         second_lowest = lowest
#         lowest = l[1]
#     elif l[1]<=second_lowest:
#         second_lowest=l[1]
# for l in lst:
#     if l[1]==second_lowest:
#         names.append(l[0])



# print(names)

# nl = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

# second = max(nl, key= lambda x: x[1])[1]
# first = min(nl, key= lambda x: x[1])[1]
    
# for i in range(len(nl)):
#     if nl[i][1] <= second and nl[i][1] != first:
#         second = nl[i][1]
    
# for i in range(len(nl)):
#     if second == nl[i][1]:
#         print(nl[i], end=", ")


# if __name__ == '__main__':
#     arr1 = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     arr1 = [name, score]
#     arr1.append(arr1)
# arr1.sort(key=lambda x: x[1])
# # print(arr)
# # print(min(arr,key=lambda x:x[1]))
# arr1.remove(min(arr1,key=lambda x:x[1]))
# # print(arr)
# minimum = min(arr1,key=lambda x:x[1])
# # print(minimum[1])
# a=[]
# minimum = minimum[1]
# for i  in arr1:
#     if(i[1] == minimum):
#         a.append(i[0])
# a.sort()
# for i in a:
#     print(i)
       

# def custom_key(second):
#     return second[1]

# nested_list = [['muskan' , 120], ['bhai' , 150] , ['ashab' , 350] , ['akaab' , 150]]


# nested_list.sort(key=custom_key)
# m = min(nested_list)
# print(m)
# n = max(nested_list)
# print(n)
# # print(nested_list[-2][0])
# # print(nested_list[-1][0])

# for marks in nested_list:
#     min 

# from itertools import permutations
 
# # Get all permutations of length 2
# # and length 2
# perm = permutations([1, 2, 3], 2)
 
# # Print the obtained permutations
# for i in list(perm):
#     print (i)
from collections import Counter

s = "aaabccddd"
a = Counter(s)
print(a)
nouse = []
use = []
for i in a.values():
    if i > 1:
        nouse.append(i)
print(nouse)




# l = []
# for i in s:
#     f = s.count(i)
#     if f > 1:
#         l.remove(f)
#     else:
#         print(f)
# print(l)  
