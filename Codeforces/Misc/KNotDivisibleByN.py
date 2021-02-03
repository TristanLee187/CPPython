t=int(input())
count=0
while count<t:
    count+=1
    l = list(map(int, input().split(' ')))
    n = l[0]
    k = l[1]
    if k<n:
        print(k)
    elif k==n:
        print(k+1)
    else:
        mul = k//(n-1)
        zoom = n*mul
        if k%(n-1)==0:
            print(zoom-1)
        else:
            zoom += k%(n-1)
            print(zoom)
    
