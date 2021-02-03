t=int(input())
count=0
while count<t:
    count+=1
    l = list(map(int, input().split(' ')))
    n = l[0]
    k = l[1]
    l = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))
    ans = sum(l)
    while k>0 and min(l)<max(l2):
        k-=1 
        ans -= l.pop(l.index(min(l)))
        ans += l2.pop(l2.index(max(l2)))
    print(ans)
