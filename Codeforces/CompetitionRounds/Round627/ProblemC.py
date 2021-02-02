t=int(input())
for c in range(t):
    moves=input()
    l=[0]
    length=len(moves)
    for i in range(length):
        if moves[i]=='R':
            l.append(i+1)
    l.append(length+1)
    jumps=[]
    for i in range(1,len(l)):
        jumps.append(l[i]-l[i-1])
    print(max(jumps))
        
