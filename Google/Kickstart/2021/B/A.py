from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    n=rn()
    s=rs()

    ans=[1]
    last=1
    for i in range(1,n):
        if s[i]>s[i-1]:
            last+=1
        else:
            last=1
        ans.append(last)
    ans=' '.join(list(map(str,ans)))

    print('Case #' + str(_+1)+': ' + str(ans))