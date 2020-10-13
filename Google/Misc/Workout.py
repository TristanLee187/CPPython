for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    diff=[l[i]-l[i-1] for i in range(1,n)]
    ans=0

    print('Case #' + str(_+1)+': ' + str(ans))