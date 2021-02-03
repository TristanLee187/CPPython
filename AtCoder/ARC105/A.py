rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

l=rl()
s=sum(l)
ans=False
for i in range(16):
    a=bin(i)[2:]
    while len(a)<4:
        a='0'+a
    su=0
    for i in range(4):
        if a[i]=='1':
            su+=l[i]
    if su==s/2:
        ans=True
yn(ans)
