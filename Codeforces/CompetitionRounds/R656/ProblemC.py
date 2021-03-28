t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    if n<=2:
        print(0)
    else:
        diffs=[]
        for i in range(1,n):
            if l[i]>l[i-1]:
                diffs.append(1)
            elif l[i]==l[i-1]:
                diffs.append(0)
            else:
                diffs.append(-1)
        i=len(diffs)-1
        while diffs[i]!=1 and i>=0:
            i-=1
        while diffs[i]!=-1 and i>=0:
            i-=1
        print(i+1)
            
        
        
        
            
        
    
