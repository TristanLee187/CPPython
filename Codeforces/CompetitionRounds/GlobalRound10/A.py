t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if len(set(l))==1:
        print(n)
    else:
        print(1)