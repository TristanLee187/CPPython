from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,q=rns()
a=rl()
t=rl()
d={}
pre=[]
h=set()
for i in range(n):
    if a[i] not in d:
        d[a[i]]=i+1
    h.add(a[i])
    pre.append(h.copy())
add=set()
ans=[]
for i in t:
    print(d)
    ans.append(d[i])
    if d[i]!=1:
        for j in pre[d[i]-1].union(add):
            d[j]+=1
        d[i]=1
        add.add(i)

print(*ans)