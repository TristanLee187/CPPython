t=int(input())
for _ in range(t):
    n=int(input())
    s1=input()
    s2=input()

    ans=0
    moves=[]
    for i in range(n):
        if s1[i]!=s2[i]:
            ans+=3
            moves.append(i+1)
            moves.append(1)
            moves.append(i+1)

    

    print(ans, end=' ')
    for i in moves:
        print(i, end=' ')
    print()
            
