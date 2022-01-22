'''
noun          ->           Class           ->          Employee
adjective     ->           Attributes      ->          name,age,salary
verb          ->           Methods         ->          getsalary(), increment()

'''
#CLASS ATTRIBUTE

class Emplyee:
    company = "Google"
    salary = 300

harry = Emplyee()
muskan = Emplyee()
#instence attribute
harry.salary = 100
muskan.salary= 200
print(harry.company)
print(muskan.company)
Emplyee.company = "youtube"
print(harry.company)
print(muskan.company)

print(harry.salary)         #harry.Attribute
print(muskan.salary)