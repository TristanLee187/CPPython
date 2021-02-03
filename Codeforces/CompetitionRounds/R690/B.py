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
    ans=False
    if '2' in s and s.index('2')==0:
        ans='020' in s and s.rindex('020')==n-3
    if not ans and '20' in s and s.index('20')==0:
        ans='20' in s and s.rindex('20')==n-2
    if not ans and '202' in s and s.index('202')==0:
        ans='0' in s and s.rindex('0')==n-1
    if not ans and '2020' in s:
        ans=True
    if len(s)<4:
        ans=False
    YN(ans)