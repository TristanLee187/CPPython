n=int(input())
a=[]
for i in range(n):
    b=input().split()
    b[1]=int(b[1])
    b[2]=int(b[2])
    a.append(b)
limits=n*[float('inf')]
for i in range(n):
    for j in range(n):
        if i!=j and a[i][0]!=a[j][0]:
            if a[i][0]=='E' and a[i][1]<a[j][1] and a[i][2]>a[j][2]:
                left=-(a[i][1]-a[j][1])
                up=a[i][2]-a[j][2]
                if up<left:
                    limits[i]=min(left,limits[i])
            elif a[i][0]=='N' and a[i][1]>a[j][1] and a[i][2]<a[j][2]:
                left=a[i][1]-a[j][1]
                up=-(a[i][2]-a[j][2])
                if left<up:
                    limits[i] = min(left, limits[i])
for i in limits:
    print(i)