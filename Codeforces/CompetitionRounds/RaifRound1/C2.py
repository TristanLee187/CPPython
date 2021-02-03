rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    s=rs()
    n=len(s)
    b=s.count('B')
    a=s.count('A')
    ans=0
    pre=0
    while pre<n and s[pre]=='B':
        pre+=1
        b-=1
    suff=0
    while s[n-suff-1]=='A' and suff<n:
        suff+=1
        a-=1
    #
    bal=0
    s=s[pre:n-suff]
    for i in s:


    #
    ans+=pre%2+suff
    print(ans)