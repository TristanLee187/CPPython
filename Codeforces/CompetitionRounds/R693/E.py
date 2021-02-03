rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
for _ in range(rn()):
    n=rn()
    p=[]
    for i in range(n):
        p.append(sorted(rl())+[i])
    p.sort(key=lambda x: x[1], reverse=True)
    p.sort(key=lambda x:x[0])
    ans=[-1]*n
    index=-1
    m=float('inf')
    for i in range(n):
        if m<p[i][1]:
            ans[p[i][2]]=index+1
        else:
            index=p[i][2]
            m=p[i][1]
    print(p)
    print(*ans)



