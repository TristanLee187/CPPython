for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans=0
    s=0
    for i in l[::-1]:
        if i>0:
            if i>-s:
                ans+=(i+s)
            s+=i
            if s>0:
                s=0
        elif i<0:
            s+=i
    print(ans)