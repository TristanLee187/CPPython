from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
@bootstrap
def elim(num, arrstr, index, index_of_a, index_of_b):
    if index==-1:
        yield 0
    if c[index] == 0:
        c[index] = num
    if arrstr == 'a':
        index_of_a[num]=-1
        index_of_b[b[index]]=-1
        yield elim(b[index], 'a', index_of_a[b[index]], index_of_a, index_of_b)
    else:
        index_of_b[num]=-1
        index_of_a[a[index]]=-1
        yield elim(a[index], 'b', index_of_b[a[index]], index_of_a, index_of_b)

for _ in range(rn()):
    n=rn()
    a=rl()
    b=rl()
    c=rl()
    index_of_a = defaultdict(int)
    for i in range(n):
        index_of_a[a[i]]=i
    index_of_b = defaultdict(int)
    for i in range(n):
        index_of_b[b[i]]=i

    for i in range(n):
        if c[i]>0:
            if a[i]==b[i]:
                index_of_b[b[i]] = -1
                index_of_a[a[i]] = -1
            elif c[i]==a[i]:
                elim(a[i], 'a', index_of_a[a[i]], index_of_a, index_of_b)
            else:
                elim(b[i], 'b', index_of_b[b[i]], index_of_a, index_of_b)
        elif a[i]==b[i]:
            c[i]=a[i]
            index_of_b[b[i]]=-1
            index_of_a[a[i]]=-1
    groups=0
    for i in range(n):
        if c[i]==0:
            groups+=1
            elim(a[i], 'a', i, index_of_a, index_of_b)

    print(pow(2,groups,mod))