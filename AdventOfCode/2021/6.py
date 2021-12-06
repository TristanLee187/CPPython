from functools import cache

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
a=list(map(int,rs().split(',')))
n=256
@cache
def solve(num,days):
    num,days = num-min(num,days), days-min(num,days)
    if days==0:
        return 1
    return solve(6,days-1)+solve(8,days-1)

for num in a:
    ans+=solve(num,n)

file.close()

print(ans)
