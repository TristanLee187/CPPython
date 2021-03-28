t = int(input())
for _ in range(t):
    p,f=map(int,input().split())
    cs,cw=map(int,input().split())
    s,w=map(int,input().split())

    ans=0
    tp=0
    tf=0
    if s<w:
        tcs=min(cs,p//s)
        tp=tcs*s
        tcw=min(cw,(p-tp)//w)
        tp+=tcw*w
        ttcs=




