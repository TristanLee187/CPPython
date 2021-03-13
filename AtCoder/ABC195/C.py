rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
d=len(str(n))
ans=0
for i in range(4,d+1):
    x=min(int(i*'9'),n)
    ans+=((i-1)//3)*(x-(int((i-1)*'9')))
print(ans)