"""
ID: tristan16
LANG: PYTHON3
PROB: palsquare
"""

a=open('palsquare.in','r')
b=open('palsquare.out','w')

base=int(a.read())

def baseChange(n,b):
    '''given an integer n, returns integer after converting to base b in the form of a string; limit base 20'''
    chars=['0','1','2','3','4','5','6','7','8','9', 'A','B','C','D','E','F','G','H','I','J']
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

for i in range(1,301):
    if isPal(baseChange(i**2,base)):
        b.write(baseChange(i,base)+' '+baseChange(i**2,base)+'\n')

        
