#creating an empty set
b = set()
print(type(b))

#adding value to the empty set
b.add(5)
b.add(4)
b.add(5)                                                                                                  #[] using this syntax for list 
b.add(5)  #adding a value does not change a set                                                           #() using this syntax for tupple                
b.add(4)        
b.add((4,6,6))   #-----this is written using tupple so this will work


# #accesing elements
# # b.add({4:5})           #we cannot add list or directory to sets                                                                                   ----- directory
# # b.add([4,5,6 ])                                                                                            ----list                
# print(b)


# #length of the set
# print(len(b))        #prints the length of this set


# #removal of the set
# b.remove(5)       #removes 5 from set b
# b.remove(15)      #throws error while trying to remove 15 (which is nt present in the set)
# print(b)


# print(b.pop())  #removes an arbitary set(kuch bhi remove karedega set meese)
# print(b)

# print(b.clear()) #will clear the set

print(b.union())    #will give the unioun of the set

print(b.intersection())
