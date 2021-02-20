rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    n=rn()
    l=rl()
    for i in range(n):
        l.append(rl())
    l.sort()
