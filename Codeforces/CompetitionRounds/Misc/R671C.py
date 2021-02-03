rl=lambda:list(map(int,input().split()))
rn=lambda:int(input())
rns=lambda:map(int,input().split())

for _ in range(rn()):
    n,k=rns()
    l=rl()
    if l.count(k)==n:
        print(0)
    elif l.count(k)>0 or sum([k-i for i in l])==0:
        print(1)
    else:
        print(2)
    
