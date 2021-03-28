n=int(input())
l=list(map(int,input().split()))
a=sorted(l)
ans=(n-1)//2
j=-1
for i in range(0,n,2):
    l[i]=a[j]
    j-=1
for i in range(1,n,2):
    l[i]=a[j]
    j-=1
print(ans)
print(' '.join(list(map(str,l))))
