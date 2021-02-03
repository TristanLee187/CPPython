t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    N = l[0]
    M = l[1]
    Q = l[2]
    p = list(map(int, input().split(' ')))
    p2 = list(map(int, input().split(' ')))
    ans = 0
    for i in p2:
        ans += N//i
    for i in p:
        for j in p2:
            if i%j==0:
                ans-=1
    print("Case #" + str(count) + ": " + str(ans))
    
