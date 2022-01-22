mydict ={
"fast" : "in a quick manner",
"muskan" : "a coder",
"marks" : [45, 56 , 56],
"anotherdict" : {'harry' : 'player'},
1 : 2         #we can also have key and value both in integer
}


#dictionary methods

# print(mydict.keys())    # this will list all the keys
# print(type(mydict.keys()))  #this will show the type but mydict here is another class
# print(list(mydict.keys()))  #this will show the list of the keys
# print(mydict.values())      #this will print the values of the dictionary
# print(mydict.items())         # this will show all the (key-value) contents of the dictionary 


#if we want to update our dictionary or add something to it using UPDATE.

# print(mydict)
# updatedVersion = {"sherpm" : "a loving person",
# "shaikh" : "surname"}
# mydict.update(updatedVersion)
# print(mydict)


print(mydict.get("fast"))  #prints value associated with key fast
print(mydict["fast"])     #prints value associated with key fast
 
# the difference between .get and [] syntax is dictionaries?

print(mydict.get("fast0"))  #returns none as fast0 is not present in the dictionary
print(mydict["fast0"])      #resturns error as  fast0 is not present in the dictionary

