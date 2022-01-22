#with "with" statement we dont have to close()




with open('another.txt' , 'r') as f:
    a  =  f.read()

with open('another.txt' , 'w') as f:
    a  =  f.write("this is me")
print(a)
