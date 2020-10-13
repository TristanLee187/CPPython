"""
ID: tristan16
LANG: PYTHON3
PROB: friday
"""
def isLeapYear(x):
    if x%400==0:
        return True
    elif x%100==0:
        return False
    elif x%4==0:
        return True
    else:
        return False

a=open('friday.in', 'r')
b=open('friday.out', 'w')

n=int(a.readline())
ans=[]
ans.extend(7*[0])
offset=1


for i in range(1900,1900+n):
    if isLeapYear(i):
        ans[(offset-2)%7]+=1
        ans[(offset+1)%7]+=1
        ans[(offset+2)%7]+=1
        ans[(offset+5)%7]+=1
        ans[(offset)%7]+=1
        ans[(offset+3)%7]+=1
        ans[(offset+5)%7]+=1
        ans[(offset+1)%7]+=1
        ans[(offset+4)%7]+=1
        ans[(offset-1)%7]+=1
        ans[(offset+2)%7]+=1
        ans[(offset+4)%7]+=1
        offset+=2
    else:
        ans[(offset-2)%7]+=1
        ans[(offset+1)%7]+=1
        ans[(offset+1)%7]+=1
        ans[(offset+4)%7]+=1
        ans[(offset-1)%7]+=1
        ans[(offset+2)%7]+=1
        ans[(offset+4)%7]+=1
        ans[(offset)%7]+=1
        ans[(offset+3)%7]+=1
        ans[(offset-2)%7]+=1
        ans[(offset+1)%7]+=1
        ans[(offset+3)%7]+=1
        offset+=1
ans.insert(0,ans.pop())
b.write(' '.join(map(str,ans)))
b.write('\n')
a.close()
b.close()

        
        
