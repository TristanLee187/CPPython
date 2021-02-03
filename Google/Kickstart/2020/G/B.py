rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    ans = 0
    n=rn()
    m=[]
    for i in range(n):
        m.append(rl())
    for i in range(n):
        pos=0
        a=n-i-1
        b=0
        while a<n and b<n:
            pos+=m[a][b]
            a+=1
            b+=1
        ans=max(pos,ans)
    for i in range(n):
        pos=0
        a=0
        b=i
        while a<n and b<n:
            pos+=m[a][b]
            a+=1
            b+=1
        ans=max(pos,ans)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
