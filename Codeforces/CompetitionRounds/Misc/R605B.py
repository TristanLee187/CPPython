for _ in range(int(input())):
    s=input()
    a=s.count('L')
    b=s.count('R')
    c=s.count('U')
    d=s.count('D')
    if min([a,b,c,d])==0:
        if (a>0 and b>0):
            print(2)
            print('RL')
        elif (c>0 and d>0):
            print(2)
            print('UD')
        else:
            print(0)
            print()
            
    else:
        ans=2*(min(a,b)+min(c,d))
        print(ans)
        print(min(a,b)*'R'+min(c,d)*'U'+min(a,b)*'L'+min(c,d)*'D')
