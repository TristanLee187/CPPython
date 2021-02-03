n,k=map(int,input().split())
a=list(map(int,input().split()))


p1=0
p2=k

for i in range(k,n):
    if a[p2]>a[p1]:
        print('Yes')
    else:
        print('No')
    p1+=1
    p2+=1



    
