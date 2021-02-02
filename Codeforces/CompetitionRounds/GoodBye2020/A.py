rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=0
    bases={}
    for i in range(n):
        for j in range(n):
            if i!=j:
                if abs(l[j]-l[i]) not in bases:
                    ans+=1
                    bases[abs(l[j]-l[i])]=1
    print(ans)
