t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    ans=[]
    for i in l:
        if i not in ans:
            ans.append(i)
    for i in ans:
        print(i,end=' ')
    print()
    
    
