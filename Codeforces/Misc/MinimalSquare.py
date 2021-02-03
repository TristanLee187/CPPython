t=int(input())
count=0
while count<t:
    count+=1
    ints = list(map(int, input().split(' ')))
    a = ints[0]
    b = ints[1]
    m = min(a,b)
    n = max(a,b)
    if 2*m>=n:
        print(4*m*m)
    elif n>=2*m:
        print(n*n)
    else:
        print(4*n*n)
