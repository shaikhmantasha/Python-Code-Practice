# #-----------------------------------------------QUESTION NO 1-----------------------------------------------------------------------------

# # from os import read


# # a = open('poems.txt')
# # b = a.read()
# # if 'twinkle' in b:
# #     print("twinkle is present")
# # else:
# #     print("twinkle is not present")
# # a.close()


# #-----------------------------------------------QUESTION NO 2-----------------------------------------------------------------------------

# # def game():
# #     return 65

# # score = game()
# # with open("highscore.txt") as f:
# #     highscore = int(f.read()) 

# # if highscore < score:
# #     with open ("highscore" , "w") as f:
# #         f.write(str(score))

#                 #---------------------if there is blank and no score-----------------

# # def game():
# #     return 65

# # score = game()
# # with open("highscore.txt") as f:
# #     highscore = f.read() 

# # if highscore=='':
# #     with open ("highscore" , "w") as f:
# #         f.write(str(score))

# # elif int(highscore) < score:
# #     with open ("highscore" , "w") as f:
# #         f.write(str(score))


# #-----------------------------------------------QUESTION NO 3-----------------------------------------------------------------------------

# # for i in range(2, 21):
# #     with open (f"multiplication_table_of{i}.txt" , 'w') as f:
# #             for j in range (1 , 11):
# #                 f.write(f"{i}X{j}={i*j}\n")
                


# #-----------------------------------------------QUESTION NO 4-----------------------------------------------------------------------------

# with open ("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey" , "@#$%^&")

# with open ("sample.txt" , 'w') as f:
#     f.write(content)


# #-----------------------------------------------QUESTION NO 5-----------------------------------------------------------------------------


# words = ["pagal" , "kaddu" , "gadha"]

# with open ("sample.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word , "@#$%^&")

# with open ("sample.txt" , 'w') as f:
#     f.write(content)


# #-----------------------------------------------QUESTION NO 6-----------------------------------------------------------------------------


# with open("log.txt") as f:
#     content = f.read().lower       #we can add lower here 

# if "python" in content.lower:       # or here      #the python in if is case sensitive
#     print("python is present")

# else:
#     print("python is not present")


# #-----------------------------------------------QUESTION NO 7-----------------------------------------------------------------------------


# #               7:57:41         ------watch video again in order to understand it
# content = True
# i = 1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if "python" in content:
#             print(content)
#             print(f"yes python is present at line {i}")
#         i+=1             # this because we want the loop to move further


# #-----------------------------------------------QUESTION NO 8-----------------------------------------------------------------------------
# how to copy a file



with open("this.txt") as f:
    content = f.read()

with open("copy.txt", 'w') as f:
    f.write(content)


# #-----------------------------------------------QUESTION NO 9-----------------------------------------------------------------------------


# how to check if the files are identical
file1 = "this.txt"
file2 = "copy.txt"

with open (file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if file1==file2:
    print("files are identical")

else:
    print("files are not identical")

# #-----------------------------------------------QUESTION NO 10-----------------------------------------------------------------------------
#how to wipe the content of the file

  
filename = "sample.txt"
with open (filename , "w") as f:
    f.read("")

# #-----------------------------------------------QUESTION NO 11-----------------------------------------------------------------------------
import os

oldname = "sample.text"
newname = "changed_by_python"

with open (oldname)as f:
    old = f.read()
with open(newname , 'w') as f:
    f.write(content)

os.remove(oldname)