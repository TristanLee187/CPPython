rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

x,y,a,b=rns()
ans=0
while x<y and x*(a-1)<b:
    ans+=1
    x*=a
diff=max(0,y-x)
from math import ceil
ans+=diff//b
if diff%b==0:
    ans-=1
print(ans)