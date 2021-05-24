from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    np = []
    p = []
    for i in a:
        if i<=0:
            np.append(i)
        else:
            p.append(i)
    np.sort()
    p.sort()

    diff = [np[i]-np[i-1] for i in range(1,len(np))]
    ans = max(1, len(np))
    if (len(diff)>0 and len(p)>0 and min(diff) >= min(p)) or (len(np)==1 and len(p)>0):
        ans = max(ans, len(np)+1)
    print(ans)
