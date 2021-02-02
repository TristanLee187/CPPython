n=int(input())
easts=[]
norths=[]
for i in range(n):
    b=input().split()
    b=[int(b[1]),int(b[2]),i,b[0]]
    if b[3]=='E':
        easts.append(b)
    else:
        norths.append(b)

easts=sorted(easts,key=lambda p:p[1])
norths=sorted(norths,key=lambda p:p[0])
ans=n*[-1]

block={}
for i in range(len(norths)):
    for j in range(len(easts)):
        if norths[i][0]>easts[i][0] and norths[i][1]<easts[i][1] and j not in block:
            if norths[i][0]-easts[i][0]<easts[i][1]-norths[i][1]:
                ans[norths[i][2]]=easts[i][1]-norths[i][1]
                break
            else:
                block[j]=1

block.clear()
for i in range(len(easts)):
    for j in range(len(norths)):
        if norths[i][0]>easts[i][0] and norths[i][1]<easts[i][1] and j not in block:
            if norths[i][0]-easts[i][0]>easts[i][1]-norths[i][1]:
                ans[easts[i][2]]=norths[i][0]-easts[i][0]
                break
            else:
                block[j]=1

for i in ans:
    if i==-1:
        print('Infinity')
    else:
        print(i)