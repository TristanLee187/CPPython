"""
ID: tristan16
LANG: PYTHON3
PROB: dualpal
"""

a=open('dualpal.in','r')
b=open('dualpal.out','w')

n,s=map(int,a.read().split())

def baseChange(n,b):
    chars=['0','1','2','3','4','5','6','7','8','9']
    ans=''
    x=n
    while x>0:
        ans = chars[x%b]+ans
        x=x//b
    return ans

def isPal(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

while n>0:
    s+=1
    count=0
    i=2
    while count<2 and i<=10:
        if isPal(baseChange(s,i)):
            count+=1
        i+=1
    if count==2:
        b.write(str(s)+'\n')
        n-=1

a.close()
b.close()
