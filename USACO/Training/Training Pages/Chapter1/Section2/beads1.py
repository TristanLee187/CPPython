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

right=0
i=0
if ids[0]=='w':
    right+=ams[0]
    i+=1
start=ids[i]
while i<len(ids) and (ids[i]=='w' or ids[i]==start):
    right+=ams[i]
    i+=1
