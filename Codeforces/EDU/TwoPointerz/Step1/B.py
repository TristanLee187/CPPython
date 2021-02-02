rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,m=rns()
a=rl()
a.append(float('inf'))
b=rl()
i=0
j=0
ans=[]
while len(ans)<m:
    while a[i]<b[j]:
        i+=1
    ans.append(i)
    j+=1
print(*ans)