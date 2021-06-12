from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

line=input().split()
line.reverse()
ans=[]
for word in line:
    add=word[::-1]
    add=add[:-1]+add[-1].lower()
    if word[0].upper()==word[0]:
        add=add[0].upper()+add[1:]
    ans.append(add)
print(*ans)