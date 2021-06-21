from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
items=[]
t=0
for i in range(n):
    items.append(rl())
    t+=items[-1][0]
items.sort(key=lambda x:(x[1],x[0]))
ans=0
acc=0
start=0
while acc<t:
    if items[start][1]<=acc:
        ans+=items[start][0]
        acc+=items[start][0]
        start+=1
    else:
        sub=min(items[start][1]-acc, items[-1][0])
        ans+=sub*2
        acc+=sub
        items[-1][0]-=sub
        if items[-1][0]==0:
            items.pop()
print(ans)