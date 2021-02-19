rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

sieve={}
for i in range(1,10**5+1):
    sieve[i]=[]
for i in range(1,10**5+1):
    for j in range(i,10**5+1,i):
        sieve[j].append(i)

for _ in range(int(input())):
    n,m,q=rns()
    miss=rl()
    read=rl()
    h={}
    for i in read:
        if i not in h:
            h[i]=0
        h[i]+=1
    ans=0
    for i in read:
        ans+=n//i
    for num in miss:
        for factor in sieve[num]:
            if factor in h:
                ans-=h[factor]
    print('Case #' + str(_ + 1) + ': ' + str(ans))