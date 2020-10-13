l = list(map(int, input().split(' ')))
a = l[0]
b = l[1]
c = l[2]
d = l[3]
count=0
s=0
if a>0:
    if d>=a:
        s+=a
        d-=a
    else:
        s+=d
        d-=d
if d>0:
    d-=b
if d>0:
    if d>=c:
        s-=c
        d-=c
    else:
        s-=d
print(s)
    
        
        
