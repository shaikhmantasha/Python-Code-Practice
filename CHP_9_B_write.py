f = open('another.txt' , 'w')                    #WRITE
f.write("write this is the up part ")
f.close()

r= open('appending.txt' , 'a')                   #APPENDING
r.write("I am appending")
r.close()