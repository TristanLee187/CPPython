for _ in range(int(input())):
    a,b=map(int,input().split())
    import math
    print(int(math.ceil(abs(b-a)/10)))