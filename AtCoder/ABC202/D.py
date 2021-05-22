from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

a,b,k=rns()
n=a+b
p=a+b
def poss(a,n):
    def fact(n):
        ans=1
        for i in range(1,n+1):
            ans*=i
        return ans
    ans=1
    for i in range(a):
        ans*=n-i
    ans //= fact(a)
    return ans
ans=''
while len(ans)<p:
    left = poss(a-1,n-1)
    right = poss(a,n-1)
    n-=1
    if a>0 and k<=left:
        ans+='a'
        a-=1
    else:
        ans+='b'
        b-=1
        k-=left
print(ans)