t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    l = list(map(int, input().split()))
    from math import ceil
    a=[[ceil(l[i]/x),i] for i in range(n)]
    a.sort()
    ans=' '.join(list(map(str,[i[1]+1 for i in a])))

    print('Case #' + str(_ + 1) + ': ' + ans)

