rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,k=rns()
    ans=''
    for i in range(n):
        if i%3==0:
            ans+='a'
        elif i%3==1:
            ans+='b'
        else:
            ans+='c'
    print(ans)