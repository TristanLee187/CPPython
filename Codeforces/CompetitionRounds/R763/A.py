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
    n,m,rb,cb,rd,cd=rns()
    ans=[]
    if rb<=rd:
        ans.append(rd-rb)
    else:
        ans.append(rb-rd+2*(n-rb))
    if cb<=cd:
        ans.append(cd-cb)
    else:
        ans.append(cb-cd+2*(m-cb))
    print(min(ans))