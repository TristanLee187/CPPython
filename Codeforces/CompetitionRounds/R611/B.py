for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=n
    a=n%k
    ans-=max(0,a-k//2)
    print(ans)
        
        
        
    
    
    
    
