t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int, input().split(' ')))

    m=-1
    ans=0
    for i in range(n):
        if l[i]>m:
            m=l[i]
            if i==n-1:
                ans+=1
            elif l[i]>l[i+1]:
                ans+=1

    print('Case #' + str(_+1)+': ' + str(ans))
        
