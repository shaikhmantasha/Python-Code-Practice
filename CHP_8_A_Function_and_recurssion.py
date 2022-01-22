def percent(marks):
    return (sum(marks)/400)*100 
#   p = (sum(marks)/400)*100 
#   return p 



# ------------------------------------------without using DEF FUNCTION-------------------------------------


# marks1 =[78,79,90,60]
# percentage1 = (sum(marks1)/400)*100

# marks2 = [45,96,68,85]
# percentage2 = (sum(marks2)/400)*100


#----------------------------------------------with using DEF FUNTION---------------------------------------

marks3 =[78,79,90,60]
percentage3 = percent(marks3)

marks4 = [45,96,68,85]
percentage4 = (sum(marks4)/400)*100

print(percentage3,percentage4)

