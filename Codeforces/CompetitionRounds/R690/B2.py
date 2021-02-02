rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    s=rs()
    ans=s[0]=='2' and s[-3:]=='020'
    ans=ans or s[:2]=='20' and s[-2:]=='20'
    ans=ans or s[:3]=='202' and s[-1:]=='0'
    ans=ans or s[:4]=='2020' or s[-4:]=='2020'
    YN(ans)