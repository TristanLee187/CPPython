from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
s=rs()
q=rn()
l=list(s[:n])
r=list(s[n:-1])
for i in range(q):
    t,a,b=rns()
    if t==1:
        if a-1>=n:
            r[a - n - 1], r[b - n - 1] = r[b - n - 1], r[a - n - 1]
        elif b-n-1>=0:
            l[a-1],r[b-n-1] = r[b-n-1],l[a-1]
        else:
            l[a-1],l[b-1] = l[b-1],l[a-1]
    else:
        l,r=r,l
print(''.join(l)+''.join(r))