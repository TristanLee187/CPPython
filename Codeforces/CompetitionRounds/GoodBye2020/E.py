rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans+=(l[i]&l[j])*(l[j]|l[k])
                ans %= (10 ** 9 + 7)
    print(ans)