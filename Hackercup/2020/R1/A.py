rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k,w=rns()
    l=rl()
    a,b,c,d=rns()
    for i in range(k,n):
        l.append((a*l[-2]+b*l[-1]+c)%d+1)
    h=rl()
    a,b,c,d=rns()
    for i in range(k,n):
        h.append((a*h[-2]+b*h[-1]+c)%d+1)
    ans=2*w+2*h[0]
    last=ans
    lasts=[ans]
    walls={}
    for i in range(1,n):
        last+=2*w+2*h[i]
        if l[i] <= l[i-1] + w:
            last-=2*min(h[i],h[i-1])+2*(l[i-1]+w-l[i])
        # if l[i] in walls and walls[l[i]]>
        last%=mod
        lasts.append(last)
        ans*=last
        ans%=mod

    print('Case #' + str(_+1)+': ' + str(ans))
    print(lasts)