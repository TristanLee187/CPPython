rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    if len(set(l))==1:
        print(-1)
    else:
        m=max(l)
        for i in range(n):
            if l[i]==m:
                if (i<n-1 and l[i]>l[i+1]) or (i>0 and l[i]>l[i-1]):
                    print(i+1)
                    break