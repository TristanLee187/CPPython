from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    sa=sorted(a)
    c=0
    ans=[]
    for i in range(n):
        num=sa[i]
        j=a.index(num,i)
        l,r,d=i+1,j+1,j-i
        if l<r:
            c+=1
            ans.append((i+1,j+1,j-i))
            old = a[i:j+1]
            old = old[j-i:]+old[:j-i]
            a[i:j+1]=old

    print(c)
    for row in ans:
        print(*row)