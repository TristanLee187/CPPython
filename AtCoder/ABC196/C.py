rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
ans=0
for i in range(1,10**6+1):
    if int(2*str(i))<=n:
        ans+=1
    else:
        break
print(ans)