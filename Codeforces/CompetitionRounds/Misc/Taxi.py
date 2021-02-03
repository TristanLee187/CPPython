
import math
n=int(input())
l=list(map(int, input().split(' ')))

b=5*[0]
for i in l:
    b[i]+=1

ans=b[4]

ans+=b[3]

b[1]-=b[3]

ans+=b[2]//2

b[2]=b[2]%2

if b[2]==1:
    ans+=1
    b[1]-=2

if b[1]<0:
    print(ans)
else:
    ans += math.ceil(b[1]/4)
    print(ans)




