n,s=map(int,input().split())
def solve(n,s):
    if s==0 or s>9*n:
        return [-1,-1]
    ans1=0
    a=n
    b=s
