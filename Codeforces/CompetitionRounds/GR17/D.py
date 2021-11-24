from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

n=rn()
a=rl()
ans=0
b=[]
o=0
for i in range(n):
    if a[i]%2==1:
        o+=1
    else:
        b.append(a[i])
ans+=(pow(2,o,mod)-1)*pow(2,len(b),mod)
ans%=mod
# tf you do with even numbers

print(ans)
print(b)