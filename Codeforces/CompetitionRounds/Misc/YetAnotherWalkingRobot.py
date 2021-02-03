def homosubstrings(s, c1, c2):
    '''Returns a list of the lengths of the contiguous substrings of character c in string s'''
    n=len(s)
    spaces=[]
    i=0
    found=False
    while i<n:
        if s[i]!=c1 and s[i]!=c2:
            spaces.append(i)
            found=True
        i+=1
    tspaces=[]
    if found:
        i=1
        if spaces[0]!=0:
            tspaces.append(spaces[0])
        while i<len(spaces):
            if spaces[i]-spaces[i-1]-1!=0:
                tspaces.append(spaces[i]-spaces[i-1]-1)
            i+=1
        if spaces[-1]!=n-1 and n-1-spaces[-1]!=0:
            tspaces.append(n-1-spaces[-1])
    elif i!=0:
        tspaces.append(i)
    return tspaces

t=int(input())
for i in range(t):
    n=int(input())
    string = input()
    diffsLR = homosubstrings(string, 'R', 'L')
    diffsUD = homosubstrings(string, 'U', 'D')
    print(diffsLR, diffsUD)
    
