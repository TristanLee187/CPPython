rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    b=rl()
    b.sort()
    s=sum(b)
    if b[-2]==s-b[-1]-b[-2]:
        print(*b[:-2])
    else:
        s-=b[-1]
        flag=False
        for i in range(n+1):
            if b[-1]==s-b[i]:
                flag=True
                b.pop(i)
                b.pop()
                break
        if flag:
            print(*b)
        else:
            print(-1)