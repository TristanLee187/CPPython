t = int(input())
for _ in range(t):
    s,a,b,x,y,c=map(int,input().split())
    l=[]
    for i in range(c):
        l.append(list(map(int,input().split())))
    ans=0
    if a==2 and b==2:
        ans=min(1,2-c)
    else:
        if x==2 and y==2:
            ans=-min(1,2-c)
        else:
            if [2,2] not in l:
                ans=2-c
    print('Case #' + str(_ + 1) + ': ' + str(ans))

