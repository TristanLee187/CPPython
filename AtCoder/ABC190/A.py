rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

a,b,c=rns()
if a>b:
    print('Takahashi')
elif b>a:
    print('Aoki')
elif c==0:
    print('Aoki')
else:
    print('Takahashi')
