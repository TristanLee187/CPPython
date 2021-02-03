for _ in range(int(input())):
    n=int(input())
    f=6
    side=1.5
    last=1
    ans=1
    c=1
    n-=1
    def quad(a, b, c):
        return int((-b + (b ** 2 - 4 * a * c) ** 0.5) // (2 * a))
    while n>0:
        if f==6:
            diff=1
        else:
            diff=2*side+1
        a=c
        if c==1 and n<6:
            a=0
        if c>1:
            q = quad(0.5, -1.5+f+diff, -n-diff+3/2)
            a = min(c, q)
        if a==0:
            break
        n-=a*f+a*(a-1)//2*diff//2
        c*=2
        ans+=a
        f=2*f+side**2
        side*=2
    print(ans)



