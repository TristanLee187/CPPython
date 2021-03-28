rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n,m=rns()
    l=[]
    for i in range(n):
        a=[]
        a.append(rl())
        a.append(rl())
        l.append(a)
    ans=False
    for i in l:
        if i==[[i[0][0],i[1][0]],[i[0][1],i[1][1]]]:
            ans=True
            break
    for i in l:
        b=[[i[0][0],i[1][0]],[i[0][1],i[1][1]]]
        if b in l:
            ans=True and ans
            break
    if m%2==1:
        ans=False
    yn(ans)
