t=int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    s=set([x,y,z])
    if len(s)==3:
        print('NO')
    elif len(s)==2 and (sum([x,y,z])-min(x,y,z))//2!=max(x,y,z):
        print('NO')
    else:
        print('YES')
        print(max(x,y,z),min(x,y,z),min(x,y,z))
    
    
