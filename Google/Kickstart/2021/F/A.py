from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    n=rn()
    s=rs()
    pre=[float('inf') if s[0]=='0' else 0]
    for i in range(1,n):
        if s[i]=='1':
            pre.append(i)
        else:
            pre.append(pre[-1])

    suff=[0 for i in range(n)]
    suff[-1]=float('inf') if s[-1]=='0' else n-1
    for i in range(n-2,-1,-1):
        if s[i]=='1':
            suff[i]=i
        else:
            suff[i]=suff[i+1]
    for i in range(n):
        ans+=min(abs(i-pre[i]),abs(i-suff[i]))
    print('Case #' + str(_+1)+': ' + str(ans))