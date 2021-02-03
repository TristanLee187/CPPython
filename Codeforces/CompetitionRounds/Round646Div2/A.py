t=int(input())
count=0
while count<t:
    def numOdds(L):
        ans=0
        for i in L:
            if i%2==1:
                ans+=1
        return ans
    

    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    x=l[1]
    l=list(map(int, input().split(' ')))
    ans=False
    o=numOdds(l)
    e=n-o

    for i in range(1, min(o, x)+1, 2):
        if e>=x-i:
            ans=True
            break
    
    
            
                    
                        
                    
                
            
        
        
    if ans:
        print("Yes")
    else:
        print("No")
            
                
        
    
