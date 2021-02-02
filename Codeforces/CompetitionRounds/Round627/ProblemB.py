def rindex(l, x):
    ans = l[::-1].index(x)
    return len(l) - 1 - ans

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split(' ')))
    ans=False
    for i in l:
        if rindex(l, i) - l.index(i)>=2:
            ans=True
            break
    if ans:
        print("YES")
    else:
        print("NO")
    
