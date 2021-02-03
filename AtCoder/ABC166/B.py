n,k=map(int,input().split())
l=n*[0]
for i in range(k):
    a=int(input())
    b=list(map(int,input().split()))
    for j in b:
        l[j-1]+=1
print(l.count(0))