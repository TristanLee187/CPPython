from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    lo=1
    hi=n
    while lo<hi:
        mid=(lo+hi)//2
        print('?',1,1,2,mid)
        one=rn()
        if one==mid+1:
            lo=mid+2
        else:
            hi=mid
    second=min(lo,hi)
    ans=n*[0]
    ans[1]=second
    # idk from here
    left=set(range(1,second))
    right=set(range(second+1,n+1))
    for i in range(n):
        if i!=1:
            print('?',1,i+1,2,second)
            one=rn()
            if one==second:
                # a+1<?
                print()
