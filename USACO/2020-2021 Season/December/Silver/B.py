n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()

ans=1
import bisect
for i in range(n):
    point=a[i]
    below=[]
    above=[]
    add=1
    for j in range(i+1,n):
        if a[j][1]<point[1]:
            k=bisect.bisect_left(below,a[j][1])
            add+=(k+1)*(len(above)+1)
            below.insert(k,a[j][1])
        else:
            k = bisect.bisect_left(above, a[j][1])
            add += (len(above) - k + 1) * (len(below) + 1)
            above.insert(k, a[j][1])
    ans+=add
print(ans)