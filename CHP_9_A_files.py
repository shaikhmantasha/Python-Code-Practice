#use open function to read the content of the file
# f = open('sample.txt' , 'r')

f = open('sample.txt')      #bydefault the mode is "r" which means read
data = f.read()             #computer usko read karega
 # date = f.read(5) #this will only read five letter
print(data)                     #phir computer usko print karega
f.close()                       #phir computer usko bund kardega

 