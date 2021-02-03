rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
towns=[]
t=0
for i in range(n):
    towns.append(rl())
    towns[-1].insert(0,sum(towns[-1])+towns[-1][0])
    t+=towns[-1][1]
towns.sort(reverse=True)

acc=0
i=0
while acc<=t:
    acc+=towns[i][0]
    i+=1
print(i)