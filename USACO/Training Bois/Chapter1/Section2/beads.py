"""
ID: tristan16
LANG: PYTHON3
PROB: beads
"""

a=open('beads.in', 'r')
b=open('beads.out', 'w')

n=int(a.readline())
s=a.readline()

ids=[]
ams=[]

last=s[0]
curr=0
for i in s:
    if i==last:
        curr+=1
    else:
        ids.append(last)
        ams.append(curr)
        curr=1
    last=i
ids.append(last)
ams.append(curr)

if len(ids)<=2:
    b.write(str(n))
else:
    
        
    


