"""
ID: tristan16
LANG: PYTHON3
PROB: namenum
"""

import bisect

file=open('dict.txt', 'r')
names=list(map(lambda x: x.strip(), file.readlines()))
file.close()

a=open('namenum.in','r')
b=open('namenum.out','w')

num=a.readline().strip()
keys=[0,0,'ABC','DEF','GHI','JKL','MNO','PRS','TUV','WXY']
ans=[]

def inc(l):
    l[-1]+=1
    if l[-1]==3:
        for i in range(len(l)-1,-1,-1):
            if l[i]==3:
                l[i]=0
                l[i-1]+=1
            else:
                break
        
    


s=[]
s.extend(len(num)*[0])
for i in range(3**len(num)):
    ts=''
    for j in range(len(num)):
        ts+=(keys[int(num[j])][int(s[j])])
    if ts==names[bisect.bisect_left(names,ts)]:
        ans.append(ts)
    inc(s)

if len(ans)>0:
    for i in ans:
        b.write(i+'\n')
else:
    b.write('NONE\n')
a.close()
b.close()


