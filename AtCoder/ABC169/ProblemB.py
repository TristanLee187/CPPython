n=int(input())
l=list(map(int, input().split(' ')))
ans=1
if 0 in l:
    print(0)
else:
    for i in l:
        ans*=i
        if ans>10**18:
            print(-1)
            break
    if not ans>10**18:
        print(ans)