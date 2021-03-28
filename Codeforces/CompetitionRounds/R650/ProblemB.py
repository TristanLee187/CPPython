t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    l=list(map(int, input().split(' ')))
    weight=0
    es=0
    os=0
    i=0
    while i<n:
        if l[i]%2!=i%2:
            weight+=1
            if l[i]%2==0:
                es+=1
            else:
                os+=1
        i+=1
    if weight%2==1 or es-os>=2 or os-es>=2:
        print(-1)
    else:
        print(weight//2)
        
        
