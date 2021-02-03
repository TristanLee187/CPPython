n=int(input())
l=list(map(int,input().split()))
for i in range(n+1):
    if i==n:
        break
    if i==n-1:
        print(l[i]*'PLR',end='')
    else:
        print(l[i]*'PRL'+'R',end='')
