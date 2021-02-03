"""
ID: tristan16
LANG: PYTHON3
PROB: gift1
"""

a=open('gift1.in', 'r')
b=open('gift1.out', 'w')

l={}

n=int(a.readline()[:-1])
for i in range(n):
    string=a.readline()[:-1]
    l[string]=0

for i in range(n):
    string=a.readline()[:-1]
    L=list(map(int, a.readline()[:-1].split(' ')))
    total=L[0]
    split = L[1]
    if split!=0:
        l[string] -= total-(total%split)
        for j in range(split):
            l[a.readline()[:-1]] += total//split

for i in l:
    b.write((i + ' ' + str(l[i])) + '\n')

b.close()
    
    
    
            
            
    
    
    

