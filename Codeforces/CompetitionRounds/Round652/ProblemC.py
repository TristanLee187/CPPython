t=int(input())
for c in range(t):
    n, k = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    w = list(map(int, input().split(' ')))

    l=sorted(l)[::-1]
    ans=0
    for i in w:
        if i==1:
            ans += 2*l.pop(0)
        else:
            ans += l.pop(0)+l.pop(-1)
    print(ans)
            
    
    
    
    
    
    
    
    
