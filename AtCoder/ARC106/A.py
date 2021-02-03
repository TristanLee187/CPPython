rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
ans=False
x=[3]
while x[-1]<n:
    x.append(3*x[-1])
y=[5]
while y[-1]<n:
    y.append(5*y[-1])
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]+y[j]==n:
            ans=True
            print(i+1,j+1)
if not ans:
    print(-1)
