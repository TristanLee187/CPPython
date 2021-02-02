n=int(input())
if n==1:
    print(2)
else:
    def factors(x):
        ans=[]
        for i in range(1,int(x**0.5)+1):
            if x%i==0:
                ans.append(i)
        tans=[]
        for j in range(len(ans)-1,-1,-1):
            if ans[j]!=x**0.5:
                tans.append(x//ans[j])
        return ans+tans
    n*=2
    f=factors(n)
    ans=0
    for i in f:
        if (n//i+1-n)%2==0:
            ans+=1
    print(2*ans)