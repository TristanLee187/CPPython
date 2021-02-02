t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    l = list(map(int, input().split(' ')))
    odds = list(filter(lambda x: x%2==1, l))
    evens = list(filter(lambda x: x%2==0, l))
    if len(odds)%2==0 and len(evens)%2==0:
        print("YES")
    else:
        l = sorted(l)
        tcount = 0
        maybe = False
        while tcount<n-1:
            if l[tcount+1]-l[tcount]==1:
                maybe = True
                break
            tcount+=1
        if maybe:
            print("YES")
        else:
            print("NO")
