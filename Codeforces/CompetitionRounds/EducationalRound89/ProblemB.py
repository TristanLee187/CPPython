t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    tcount = 0
    ans=1
    left=l[1]
    right=l[1]
    while tcount<l[2]:
        tcount+=1
        L=list(map(int, input().split(' ')))
        nleft=L[0]
        nright=L[1]
        if nleft<=left and nright>=right:
            ans += left-nleft + nright-right
            left = nleft
            right = nright
        elif nleft<left and nright>=left:
            ans += left-nleft
            left = nleft
        elif nright>right and nleft<=right:
            ans += nright-right
            right = nright
    print(ans)
        
        
