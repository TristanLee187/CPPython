rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    s=rs()
    a=[0]
    last=s[0]
    for i in s:
        if i==last:
            a[-1]+=1
        else:
            last=i
            a.append(1)
    print(max(a)-1)