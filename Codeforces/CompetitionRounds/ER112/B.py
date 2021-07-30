from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    W,H=rns()
    a,b,c,d=rns()
    w,h=rns()

    ans=float('inf')
#     bottom left
    if a>=w or b>=h:
        ans=0
    else:
        if w-a<=W-c:
            ans=min(ans, w-a)
        if h-b<=H-d:
            ans=min(ans, h-b)
#   top left
    if a>=w or d<=H-h:
        ans=0
    else:
        if w-a<=W-c:
            ans=min(ans, w-a)
        if b>=d-(H-h):
            ans=min(ans, d-(H-h))
#   top right
    if W-w>=c or H-h>=d:
        ans=0
    else:
        if a>=c-(W-w):
            ans=min(ans, c-(W-w))
        if b>=d-(H-h):
            ans=min(ans, d-(H-h))
#   bottom right
    if W-w>=c or b>=h:
        ans=0
    else:
        if a>=c-(W-w):
            ans=min(ans, c-(W-w))
        if h-b<=H-d:
            ans=min(ans, h-b)
    if ans==float('inf'):
        print(-1)
    else:
        print(ans)

