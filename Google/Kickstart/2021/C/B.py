from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    ans=0
    g=rn()
    b=[]
    for test in range(1,int((8*g+1)**0.5)+1):
        a=g/test-(test-1)/2
        if a==int(a) and a>0:
            ans+=1
            b.append(a)

    print('Case #' + str(_+1)+': ' + str(ans))