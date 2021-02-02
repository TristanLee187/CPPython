t=int(input())
count=0
while count<t:
    count+=1
    l = list(map(int, input().split(' ')))
    N = l[0]
    K = l[1]
    vals = list(map(int, input().split(' ')))
    tcount = 0
    ans=0
    on=vals[tcount]==K
    while tcount<N-1:
        diff = vals[tcount]-vals[tcount+1]
        if diff==1 and on:
            if vals[tcount+1]==1:
                ans+=1
                on=False
        else:
            if vals[tcount+1]==K:
                on=True
            else:
                on=False
        tcount+=1
    print("Case #"+str(count)+": "+str(ans))
    

            
    
