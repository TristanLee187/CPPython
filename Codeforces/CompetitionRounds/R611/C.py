n=int(input())
l=list(map(int,input().split()))
a=len(l)*[0]
for i in l:
    if i!=0:
        a[i-1]=1
a=[i+1 for i in range(len(l)) if a[i]==0]
b=[i+1 for i in range(len(l)) if l[i]==0]

#fix
for i in range(len(a)):
    if a[i]==b[i]:
        temp=a[(i+1)%len(a)]
        a[(i+1)%len(a)]=a[i]
        a[i]=temp

for i in range(len(a)):
    l[b[i]-1]=a[i]
print(' '.join(list(map(str,l))))
