t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int, input().split(' ')))

    ans=-1

    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            ans=i
            break

    if ans==-1:
        print('NO')
    else:
        print('yes')
        print(i,i+1,i+2)
            
            
 
                
        
                
                
