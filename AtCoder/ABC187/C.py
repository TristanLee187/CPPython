rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
d={}
for i in range(n):
    s=rs()
    if s[0]=='!':
        if s[1:] in d:
            d[s[1:]]+=[s]
        else:
            d[s[1:]]=[s]
    else:
        if s in d:
            d[s]+=[s]
        else:
            d[s]=[s]
ans=True
pans=''
for i in d:
    if len(set(d[i]))>1:
        ans=False
        pans=i
        break
if ans:
    print('satisfiable')
else:
    print(pans)