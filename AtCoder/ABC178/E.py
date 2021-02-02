n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
a=sorted([l[i][::-1] for i in range(n)])

points=[l[0]]
for i in range(1,n):
    if l[i][0]!=l[0][0]:
        points.append(l[i-1])
        break
points.append(l[-1])
for i in range(n-1,-1,-1):
    if l[i][0]!=l[-1][0]:
        points.append(l[i+1])
        break
points.append(a[0])
for i in range(1,n):
    if a[i][0]!=a[0][0]:
        points.append(a[i-1])
        break
points.append(a[-1])
for i in range(n-1,-1,-1):
    if a[i][0]!=a[-1][0]:
        points.append(a[i+1])
        break

def f(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
ans=0
for i in l:
    for j in points:
        ans=max(ans,f(i,j))
print(ans)