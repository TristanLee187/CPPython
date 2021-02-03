rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    ans=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and (len(ans)==0 or i%ans[-1]==0):
            ans.append(i)
            n/=i
    if len(ans)==0:
