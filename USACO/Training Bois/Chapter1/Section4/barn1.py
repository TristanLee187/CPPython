"""
ID: tristan16
LANG: PYTHON3
PROB: barn1
"""

a=open('barn1.in','r')
b=open('barn1.out','w')

m,s,c=map(int,a.readline().split())

l=[]

for i in range(c):
    l.append(int(a.readline()))
l=sorted(l)

spaces=[]
for i in range(1,c):
    spaces.append(l[i]-l[i-1]-1)
spaces=sorted(spaces)[::-1]
ans=l[-1]-l[0]+1
i=0
while i<len(spaces) and i<m-1:
    ans-=spaces[i]
    i+=1



b.write(str(ans)+'\n')

a.close()
b.close()
