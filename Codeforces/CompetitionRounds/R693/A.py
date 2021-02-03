rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    w,h,n=rns()
    c=1
    wc=0
    while w%2==0:
        w=w//2
        wc+=1
    hc=0
    while h%2==0:
        h=h//2
        hc+=1
    if wc>0:
        c*=2**wc
    if hc>0:
        c*=2**hc
    YN(c>=n)