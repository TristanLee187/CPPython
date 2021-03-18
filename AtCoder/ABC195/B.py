rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))
from math import ceil
a,b,w=rns()
w*=1000
if w>=a:
    mi=ceil(w/b)
    ma=ceil(w//a)
    if mi<=ma:
        print(mi,ma)
    else:
        print('UNSATISFIABLE')

else:
    print('UNSATISFIABLE')