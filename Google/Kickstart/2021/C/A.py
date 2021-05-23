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
    ans=0
    n,k=rns()
    s=rs()[:-1]
    for i in range(n//2+n%2):
        c=ord(s[i])-97
        ans+=c*pow(k,(n//2+n%2-i-1),10**9+7)
        ans %= 10 ** 9 + 7
    comp=s[:n//2]
    if n%2==0:
        t=comp+comp[::-1]
    else:
        t=comp+s[n//2]+comp[::-1]
    if t<s:
        ans+=1
        ans%=10**9+7
    print('Case #' + str(_+1)+': ' + str(ans))
