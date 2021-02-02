t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        ans=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                ans=i
                break
        if ans==1:
            print(1,n-1)
        else:
            print(n//ans, n-n//ans)
        
        
        
    
    
