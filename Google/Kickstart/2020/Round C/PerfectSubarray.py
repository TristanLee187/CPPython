t=int(input())
count=0
while count<t:
    count+=1
    N=int(input())
    l=list(map(int, input().split(' ')))
    point1=0
    point2=0
    ans=0
    while point1<N and point2<N:
        maybe=0
        while point2<N:
            maybe+=l[point2]
            point2+=1
            if maybe>=0 and (maybe**0.5)%1==0:
                ans+=1
        point1+=1
        point2=point1
    print("Case #" + str(count) + ": " + str(ans))
        
