rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    l=rl()
    a=sorted(l)
    s=set()
    ans=[]
    i=n-1
    slice=[]
    while i>=0:
        slice.append(l[i])
        s.add(l[i])
        if l[i]==a[-1]:
            ans+=slice[::-1]
            slice.clear()
            a.pop()
            while len(a)>0 and a[-1] in s:
                a.pop()
        i-=1
    print(*(ans+slice[::-1]))