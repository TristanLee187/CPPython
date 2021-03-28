t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    a=l[0]
    b=l[1]
    c = max(a,b)
    d=min(a,b)
    if c>=2*d:
        print(d)
    else:
        ans = c-d
        d-=ans
        c-=2*ans
        ans+=2*(c//3)
        c=c%3
        d=d%3
        if c+d>2:
            ans+=1
        print(ans)
    
    
    
