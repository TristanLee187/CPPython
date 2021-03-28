t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    if n<=2:
        print(0)
    else:
        def isGood(l):
            return l[1]!=min(l) or len(set(l))==1

        ans=0
        if isGood(l[n-3:]):
            for i in range(n-3):
                if l[i]>l[i+1]:
                    ans=i+1
        else:
            for i in range(n-2):
                if l[i]>l[i+1]:
                    ans=i+1
        print(ans)
            
            
                
            
            
        
        
    
    
