rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(int(input())):
    from bisect import bisect_left
    n,m,q=rns()
    miss=rl()
    read=rl()
    ans=0
    for num in read:
        for i in range(1,n//num+1):
            j=bisect_left(miss,i*num)
            if j==len(miss) or miss[j]!=i*num:
                ans+=1
    print('Case #' + str(_ + 1) + ': ' + str(ans))

