"""
ID: tristan16
LANG: PYTHON3
PROB: friday
"""

year=1900

def isLeapYear(x):
    if x%400==0:
        return True
    elif x%100==0:
        return False
    elif x%4==0:
        return True
    else:
        return False

a=open('friday.in', 'r')
b=open('friday.out', 'w')

n=int(a.readline()[:-1])

day=2

