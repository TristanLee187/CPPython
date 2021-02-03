rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

a,b=rns()
n=0
for i in str(a):
    n+=int(i)
m=0
for i in str(b):
    m+=int(i)
print(max(n,m))