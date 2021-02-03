rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
l=rl()
l.sort()
for i in range(n):
    l[i] = l[i] % l[0] + l[0]
l.sort()
while l[0]!=l[-1]:
    a=l[-1]-l[0]
    l=[a]+[i-a for i in l[:-1]]
    l.sort()
    for i in range(n):
        l[i]=l[i]%l[0]+l[0]
    l.sort()
print(l[0])