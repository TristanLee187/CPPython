from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

n,q=rns()
s=list(rs())
ans=0
for i in range(n-2):
    if s[i:i+3]==['a','b','c']:
        ans+=1
# print(se)
for _ in range(q):
    a,b=rs().split()
    a=int(a)-1
    before = []
    for i in range(-2,1):
        if 0<=a+i and a+i+2<n:
            before.append(s[a+i:a+i+3])
    bb=['a','b','c'] in before

    after=[]
    s[a]=b
    for i in range(-2,1):
        if 0<=a+i and a+i+2<n:
            after.append(s[a+i:a+i+3])
    cc=['a','b','c'] in after
    ans+=cc-bb
    print(ans)
