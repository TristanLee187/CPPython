rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,w=rns()
    l=rl()
    for i in range(n):
        l[i]=[l[i],i+1]
    l.sort()
    s=0
    ans=[]
    for i in range(n):
        s+=l[i][0]
        ans.append(l[i][1])
        if s>w:
            if w>=l[i][0]>=w/2:
                ans=[l[i][1]]
            else:
                ans=[-1]
            break
        elif s>=w/2:
            break
    if s<w/2:
        ans=[-1]
    if ans!=[-1]:
        print(len(ans))
    print(*ans)