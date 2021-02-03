rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    s=rs()
    t=rs()
    a=[]
    for i in range(1,len(s)+1):
        sub=s[:i]
        if s==sub*(len(s)//i):
            a.append(sub)
    b=[]
    for i in range(1,len(t)+1):
        sub=t[:i]
        if t==sub*(len(t)//i):
            b.append(sub)
    sub=''
    for i in a:
        if i in b:
            sub=i
    if sub=='':
        print(-1)
    else:
        x=len(s)//len(sub)
        y=len(t)//len(sub)
        print(x*y*sub)
