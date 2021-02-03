rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n,s,d=rns()
moves=[]
for i in range(n):
    moves.append(rl())
ans=False
for i in moves:
    if i[0]<s and i[1]>d:
        ans=True
        break
yn(ans)