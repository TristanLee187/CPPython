from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n,k,x=rns()
    x-=1
    s=rs()
    acc=[]
    ids=[]
    last=s[0]
    c=0
    for i in range(n+1):
        if i==n:
            acc.append(c)
            ids.append(last)
        elif s[i]==last:
            c+=1
        else:
            acc.append(c)
            c=1
            ids.append(last)
            last=s[i]
    ans=''
    while acc:
        if ids[-1]=='a':
            ans+=acc[-1]*'a'
            ids.pop()
            acc.pop()
        else:
            m=max(0,x%(acc[-1]*k+1))
            ans+=m*'b'
            x//=((acc[-1]*k)+1)
            acc.pop()
            ids.pop()
    print(ans[::-1])
