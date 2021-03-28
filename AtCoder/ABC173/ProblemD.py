n=int(input())
l=list(map(int, input().split(' ')))

l=sorted(l)[::-1]

ans=l[0]
a=2

for i in range(1,n):
    ans+=(min(2,n-a))*l[i]
    a+=min(2,n-a)
    if a==n:
        break

print(ans)
    

