from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    input()
    n,k=rns()
    a=rl()
    t=rl()
    data=sorted(zip(a,t))
    # lefts
    lm=[float('inf')]
    i=0
    for j in range(n):
        if i<k and data[i][0]==j+1:
            lm.append(min(lm[-1]+1, data[i][1]))
            i += 1
        else:
            lm.append(lm[-1]+1)
    lm.pop(0)
    # rights
    rm=[float('inf')]
    i=k-1
    for j in range(n-1,-1,-1):
        if data[i][0]==j+1:
            rm.append(min(rm[-1]+1, data[i][1]))
            i -= 1
        else:
            rm.append(rm[-1]+1)
    rm.reverse()
    rm.pop()

    ans=[]
    for i in range(n):
        ans.append(min(rm[i], lm[i]))
    print(*ans)
