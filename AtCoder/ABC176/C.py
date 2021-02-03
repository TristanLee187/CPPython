n=int(input())
l=list(map(int,input().split()))
def solve(n,l):
     if n==1:
        return 0
     ans=0
     m=0
     for i in range(n):
         if l[i]>=m:
            m=l[i]
         else:
            ans+=max(0,m-l[i])
     return ans
print(solve(n,l))