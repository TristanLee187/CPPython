rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,m=rns()
a=rl()
b=rl()
a.append(float('inf'))
b.append(float('inf'))
ans=[]
i=0
j=0
while len(ans)<n+m:
    if a[i]<b[j]:
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1
print(*ans)