from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rs()
    a=''
    b=''
    for i in range(len(n)):
        if i&1:
            a+=n[i]
        else:
            b+=n[i]
    # if len(n)&1 and a=='0':
    #     a+='0'
    # if len(n)&1==0 and b=='0':
    #     b+='0'

    def f(s):
        if not s:
            return 1
        return int(s)+1
    ans=f(a)*f(b)

    print(max(ans-2,0))
