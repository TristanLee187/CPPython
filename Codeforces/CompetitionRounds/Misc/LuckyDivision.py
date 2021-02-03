n=int(input())

ans=False

def isLucky(x):
    for i in x:
        if i!='4' and i!='7':
            return False
    return True
    

for i in range(1, int(n**0.5+1)):
    if n%i==0:
        if isLucky(str(i)) or isLucky(str(n//i)):
            ans=True
            break

if ans:
    print("YES")
else:
    print('NO')
    
