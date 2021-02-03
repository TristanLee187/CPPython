n=int(input())

def fact(n):
    ans=1
    for i in range(2,n+1):
        ans*=i
    return ans

ans=fact(n-1)

if ans>1:
    ans/=(n/2)

print(int(ans))

