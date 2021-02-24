rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


a,b,k=rns()
if k==0:
    print('Yes')
    s=b*'1'+a*'0'
    print(s)
    print(s)
elif k>a+b-2 or b==1 or a==0:
    print('No')
else:
    print('Yes')
    s1=b*'1'+a*'0'
    s2=''
    if k<=a:
        s2+=(b-1)*'1'
        s2+=k*'0'+'1'
        s2+=(len(s1)-len(s2))*'0'
    else:
        tail=(a-1)*'0'+'1'
        k-=len(tail)
        s2+=(b-1-k)*'1'+'0'+k*'1'
        s2+=tail
    print(s1)
    print(s2)