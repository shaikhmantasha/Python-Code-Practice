#  Sun 10 May 2015 13:54:36 -0700
#   %a %d %b   %Y  %h %m %s  %z                  %TIME ZONe - every area has its different time zone


# QUESTION :
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000


#ANSWERRRRR

from datetime import datetime


def time_delta(t1 , t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    tame1 = datetime.strptime(t1 , time_format)
    tame2 = datetime.strptime(t2 , time_format)
    return int(abs(tame1 - tame2).total_seconds())

for i in range(int(input())):
    t1 = input()
    t2 = input()
    print(time_delta(t1 , t2))



