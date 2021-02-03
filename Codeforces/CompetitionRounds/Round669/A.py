for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n==2:
        if 0 in l:
            print(1)
            print(0)
        else:
            print(2)
            print(' '.join(list(map(str,l))))
    elif l.count(1)>l.count(0):
        print(n-l.count(0)-l.count(0)%2)
        print(' '.join(list(map(str,(l.count(1)-l.count(0)%2)*[1]))))
    else:
        print(n-l.count(1))
        print(' '.join(list(map(str, (l.count(0)) * [0]))))
