t=int(input())
for _ in range(t):
    n,x=map(int, input().split(' '))
    l=list(map(int,input().split(' ')))

    l=sorted(l)

    ans=0
    count=1

    for i in range(n-1,-1,-1):
         if l[i]*count>=x:
             ans+=1
             count=1
         else:
             count+=1

    print(ans)
            

    
