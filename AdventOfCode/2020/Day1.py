a=[]
for i in range(200):
    a.append(int(input()))
a.sort()
for i in range(200):
    for j in range(200):
        for k in range(200):
            if j!=i!=k:
                if a[i]+a[j]+a[k]==2020:
                    print(a[j]*a[i]*a[k])
                    print(a[j],a[i])
                    break