n=int(input())
def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
        ans%=10**9+7
    return ans%(10**9+7)

print((factorial(n)-((2**(n-1))%(10**9+7)))%(10**9+7))
