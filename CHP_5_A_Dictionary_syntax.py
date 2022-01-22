 #diactionary means key = word , meaning = value

mydict ={
"fast" : "in a quick manner",
"muskan" : "a coder",
"marks" : [45, 56 , 56],
"anotherdict" : {'harry' : 'player'}     #we can also write dictionary form
}
print(mydict['fast'])
print(mydict['muskan'])
print(mydict['marks'])
print(mydict['anotherdict']['harry'])

#dictionary is mutable means it cahange the value

mydict['marks'] = [456,75]
print(mydict['marks'])

