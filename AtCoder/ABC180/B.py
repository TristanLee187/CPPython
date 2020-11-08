rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

n=rn()
l=rl()
a=0
b=0
c=0
for i in l:
    a+=abs(i)
    b+=i**2
    c=max(c,abs(i))
b=b**0.5
print(a)
print(b)
print(c)