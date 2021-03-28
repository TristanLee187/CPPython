rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    a,b,c=rns()
    import math
    ans=(b**2+(a-c)**2)**0.5
    ans=math.ceil(ans)
    print(ans)