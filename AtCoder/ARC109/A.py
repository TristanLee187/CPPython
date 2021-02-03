rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

a,b,x,y=rns()
ans=0
if a>b:
    a-=1
    ans+=x
    if 2*x>y:
        ans+=(a-b)*y
    else:
        ans+=(a-b)*2*x
else:
    if 2*x>y:
        ans+=-(a-b)*y
    else:
        ans+=-(a-b)*2*x
    ans+=x

print(ans)