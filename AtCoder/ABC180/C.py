rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

n=rn()
a=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        print(i)
        a.append(i)
for i in a[::-1]:
    if n//i!=i:
        print(n//i)