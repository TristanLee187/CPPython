rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,a,b,h=rns()
    s=rs()
    if a<b:
        z=s.count('0')
        o=s.count('1')
        ans=z*a+o*h+o*a
        print(min(ans,z*a+o*b))
    elif a>b:
        z = s.count('0')
        o = s.count('1')
        ans=z * h + o * b+z*b
        print(min(ans,z*a+o*b))
    else:
        print(n*a)