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
    n=rn()
    a=rl()
    s=set(range(1,n+1))
    extra=[]
    for i in a:
        if i in s:
            s.remove(i)
        else:
            extra.append(i)
    extra.sort()
    s=sorted(list(s))
    ans=0
    for i in range(len(extra)):
        if extra[i]/2 <= s[i]:
            ans=-1
            break
        ans+=1
    print(ans)