t = int(input())
count=0
while count<t:
    count+=1
    l = list(map(int, input().split(' ')))
    n = l[0]
    k = l[1]
    if n==1:
        print(0)
    elif n==2:
        print(k)
    elif n%2==0:
        print(max(1+2*(k-1), 2*k))
    else:
        print(2*k)
