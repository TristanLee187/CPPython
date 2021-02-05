rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

for _ in range(rn()):
    x,y=rns()
    s=rs()
    a=0
    b=0
    for i in s:
        if i=='R':
            a+=1
        elif i=='L':
            a-=1
        elif i=='U':
            b+=1
        else:
            b-=1
    ans=False
    hor=a-x
    if hor>=0:
        ans=s.count('R')>=hor
    else:
        ans=s.count('L')>=abs(hor)
    ver=b-y
    if ver>=0:
        ans = ans and s.count('U')>=ver
    else:
        ans=ans and s.count('D')>=abs(ver)
    YN(ans)