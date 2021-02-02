n=int(input())
c=0
ans=False
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        c+=1
    else:
        c=0
    if c==3:
        ans=True
if ans:
    print('Yes')
else:
    print('No')