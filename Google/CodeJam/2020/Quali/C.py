rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    n=rn()
    l=[]
    for i in range(n):
        l.append(rl()+[i])
    l.sort()
    flag=True
    ans=n*['']
    right=-1
    for i in range(n):
        if l[i][0]>=right:
            ans[i]='C'
            right=l[i][1]
        else:
            ans[i]='J'
    right=-1
    for i in range(n):
        if ans[i]=='J':
            if l[i][0]<right:
                flag=False
                break
            else:
                right=l[i][1]
    if not flag:
        ans='IMPOSSIBLE'
    else:
        pans=n*['']
        for i in range(n):
            pans[l[i][2]]=ans[i]
        ans = ''.join(pans)
    print('Case #' + str(_ + 1) + ': ' + ans)