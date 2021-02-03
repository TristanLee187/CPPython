rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
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
    n=rn()
    ans='989'
    if n>2:
        n-=3
        add='9876543210'[::-1]
        ans+=(n//10)*add
        ans+=add[:n%10]
    else:
        ans=ans[:n]
    print(ans)