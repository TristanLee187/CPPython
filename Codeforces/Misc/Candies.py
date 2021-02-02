t = int(input())
count = 0

while count<t:
    count+=1
    n = int(input())
    k = 2
    x = n/(2**k-1)
    while int(x) != x:
        k += 1
        x = n/(2**k-1)
    print(int(x))
