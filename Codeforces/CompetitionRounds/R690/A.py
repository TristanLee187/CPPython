rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    l=rl()
    left=0
    right=n-1
    ans=[]
    for i in range(n):
        if i%2==0:
            ans.append(l[left])
            left+=1
        else:
            ans.append(l[right])
            right-=1
    print(*ans)