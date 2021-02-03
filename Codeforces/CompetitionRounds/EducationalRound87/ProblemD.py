import bisect

n,q = map(int, input().split(' '))

l=list(map(int, input().split(' ')))

sums=0
for i in l:
    if i>0:
        sums+=1
    else:
        sums-=1
if sums+n<=0:
    print(0)
else:
    
    l=sorted(l)



    qus = list(map(int, input().split(' ')))

    for i in qus:
        if i>0:
            l.insert(bisect.bisect_left(l, i), i)
        else:
            l.pop(-i-1)

    if len(l)==0:
        print(0)
    else:
        print(l[0])
            
    
