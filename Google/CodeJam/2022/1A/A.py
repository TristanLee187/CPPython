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
    ans=''
    s=rs()
    n=len(s)
    ids=[s[0]]
    accs=[1]
    for i in range(1,n):
        if s[i]==ids[-1]:
            accs[-1]+=1
        else:
            ids.append(s[i])
            accs.append(1)
    for i in range(len(ids)):
        if i<len(ids)-1 and ids[i]<ids[i+1]:
            ans+=2*accs[i]*ids[i]
        else:
            ans+=accs[i]*ids[i]
    print('Case #' + str(_+1)+': ' + ans)