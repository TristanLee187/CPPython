rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

from bisect import bisect_left
for _ in range(rn()):
    n,m=rns()
    a=[]
    for i in range(n):
        a.append(rl())
    acc=[]
    for i in range(n):
        acc.append([a[i][0],1])
        acc.append([a[i][1],0])
    acc.sort()
    indexes=[i[0] for i in acc]
    pre=[]
    lines=[]
    curr=0
    ones=0
    for i in range(len(acc)-1):
        pre.append(curr)
        lines.append(ones)
        if acc[i][1]==1:
            ones+=1
        else:
            ones-=1
        curr+=ones*(acc[i+1][0]-acc[i][0])
    pre.append(curr)
    lines.append(ones)
    b=[]
    for i in range(m):
        b.append(rl())
    ans=0
    for entry in b:
        left=0
        i=bisect_left(indexes,entry[0])
        if i==len(indexes):
            left=pre[-1]
        else:
            if i>0 and indexes[i]!=entry[0]:
                i-=1
            left=pre[i]+max(entry[0]-indexes[i],0)*lines[min(i+1,len(lines)-1)]
        j=bisect_left(indexes,entry[1])
        right=0
        if j==len(indexes):
            right=pre[-1]
        else:
            if j>0 and indexes[j]!=entry[1]:
                j-=1
            right=pre[j]+max(entry[1]-indexes[j],0)*lines[min(j+1,len(lines)-1)]
        ans+=right-left
    print(ans)