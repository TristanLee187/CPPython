t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    m=l[1]
    one=l[2]
    two=l[3]
    board = []
    for i in range(n):
        board.append(input())
    prof = min(2*one,two)
    ans=0
    for i in board:
        if m==1 and i[0]=='.':
            ans+=one
        else:
            j=0
            while j<m:
                if j==m-1:
                    if i[j]=='.':
                        ans+=one
                elif i[j]=='.':
                    if i[j+1]=='.':
                        ans+=prof
                        j+=1
                    else:
                        ans+=one
                j+=1
    print(ans)
            
        
