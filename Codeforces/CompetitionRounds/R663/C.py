n=int(input())
def sumCounting(x):
    return x*(x+1)//2
def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
        ans%=(10**9+7)
    return ans%(10**9+7)
ans=sumCounting(n-2)
add=ans
sub=0
while add>0:
    ans+=add
    sub+=1
    add-=sub
ans=ans%(10**9+7)
ans*=(n-2)
ans%=(10**9+7)
ans*=factorial(n-3)
ans=ans%(10**9+7)
print(ans)