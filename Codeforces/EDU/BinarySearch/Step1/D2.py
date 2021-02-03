n=int(input())
l=list(map(int,input().split()))
l.sort()
k=int(input())

ans=[]
from bisect import *
for i in range(k):
    left,right=map(int,input().split())
    ans.append(bisect_right(l,right)-bisect_left(l,left))

print(' '.join(list(map(str,ans))))