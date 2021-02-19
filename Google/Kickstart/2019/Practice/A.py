t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    n=int(input())
    while a<=b:
        mid=(a+b+1)//2
        print(mid)
        s=input()
        if s=='TOO_SMALL':
            a=mid+1
        elif s=='TOO_BIG':
            b=mid-1
        else:
            break