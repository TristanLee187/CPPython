rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    b=rs()
    ans='1'
    d=str(int(b[0])+int(ans[0]))
    for i in range(1,n):
        if int(b[i])+1==int(d[-1]):
            ans+='0'
            d+=str(int(b[i]))
        else:
            ans+='1'
            d+=str(int(b[i])+1)
    print(ans)