rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n,k=rns()
    pre=n-k
    ans=[]
    for i in range(1,k-pre):
        ans.append(i)
    for i in range(k,k-pre-1,-1):
        ans.append(i)
    print(*ans)