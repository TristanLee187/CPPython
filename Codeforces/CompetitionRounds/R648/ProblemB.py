def maybe(l, L, b, x, y):
    i = L.index(l[0])
    j = b[i]
    if b[0]!=j:
        l.pop(0)
        L.pop(i)
        b.pop(i)
        if j==0:
            return maybe(l, L, b, x-1, y)
        else:
            return maybe(l, L, b, x, y-1)
    else:
        
    
    


t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    
    c = sorted(a)
    x=0
    y=0
    for i in b:
        if i==0:
            x+=1
        else:
            y+=1
    
    
    
    
    
    
    
