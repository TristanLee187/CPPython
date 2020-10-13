k=int(input())
l=list(map(int, input().split(' ')))
a=l[0]
b=l[1]

if (b-a)+1>=k:
    print('OK')
else:
    maybe=(a//k)*k
    ans=False
    while maybe<=b:
        if maybe>=a:
            ans=True
            break
        else:
            maybe+=k
    if ans:
        print('OK')
    else:
        print('NG')
