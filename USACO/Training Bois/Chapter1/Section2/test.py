"""
ID: tristan16
LANG: PYTHON3
TASK: test
"""

a=open('test.in', 'r')
b=open('test.out', 'w')
l=list(map(int, a.readline().split(' ')))
x=l[0]
y=l[1]
s=x+y
b.write(str(s)+'\n')
b.close()
