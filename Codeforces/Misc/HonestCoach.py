t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    l = list(map(int, input().split(' ')))
    l = sorted(l)
    ans = max(l)
    tcount=0
    while tcount<n-1:
        comp = l[tcount+1]-l[tcount]
        if comp<ans:
            ans=comp
        tcount+=1
    print(ans)
        
