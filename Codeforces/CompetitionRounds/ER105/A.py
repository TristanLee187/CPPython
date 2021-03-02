rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    ans=False
    h=[]
    for i in range(len(s)):
        if s[i]!=s[0] and s[i] not in h:
            h.append(s[i])
        if len(h)==2:
            break
    def f(s):
        bal=0
        for i in s:
            if i=='(':
                bal+=1
            else:
                bal-=1
            if bal<0:
                return False
        return bal==0
    s=s.replace(s[0],'(')
    if len(h)==1:
        b=s.replace(h[0],')')
        ans=ans or f(b)
    elif len(h)==2:
        b = s.replace(h[0], ')')
        b = b.replace(h[1], '(')
        ans = ans or f(b)
        b = s.replace(h[0], ')')
        b = b.replace(h[1], ')')
        ans = ans or f(b)
        b = s.replace(h[0], '(')
        b = b.replace(h[1], ')')
        ans = ans or f(b)
        b = s.replace(h[0], '(')
        b = b.replace(h[1], '(')
        ans = ans or f(b)
    YN(ans)