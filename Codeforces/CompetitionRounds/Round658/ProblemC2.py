t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    t=input()

    moves=[]
    for i in range(n-1):
        if s[i]!=s[i+1]:
            moves.append(i+1)

    if s[-1]!=t[-1]:
        moves.append(n)

    last=t[-1]

    for i in range(n-2,-1,-1):
        if t[i]!=last:
            moves.append(i+1)
            if last=='1':
                last='0'
            else:
                last='1'
            

    print(len(moves), ' '.join(map(str,moves)))
        
        
