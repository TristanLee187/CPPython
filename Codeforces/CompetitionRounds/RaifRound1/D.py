rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
l=rl()
ans=[]
row=n
col=n
index=0
flag=True
for i in range(n):
    if l[i]==0:
        index-=1
    elif l[i]==1:
        if len(ans)==0 or ans[-1][1]!=col:
            ans.append([row,col,i])
    elif l[i]==2:
        if len(ans)==0 or ans[-1][1]!=col:
            ans.append([row,col,i])
        while index<n-1 and l[index+1]==0:
            col-=1
            index+=1
        col-=1
        ans.append([row, col,i])
    else:
        if len(ans)==0 or ans[-1][1]!=col:
            ans.append([row,col,i])
        while index < n - 1 and l[index + 1] == 0:
            col -= 1
            index+=1
        col-=1
        ans.append([row, col,i])
        row-=1
        ans.append([row, col,i])
    if row<=0 or col<=0:
        flag=False
    index+=1
if flag:
    print(len(ans))
    for i in ans:
        pl(i)
else:
    print(-1)