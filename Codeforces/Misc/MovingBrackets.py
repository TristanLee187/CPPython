t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    numL=0
    ans=0
    for i in s:
        if i==')':
            if numL==0:
                ans+=1
            else:
                numL-=1
        else:
            if numL==0:
                numL=1
            else:
                numL+=1
    print(ans)
            
                
            
