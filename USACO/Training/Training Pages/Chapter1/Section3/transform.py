"""
ID: tristan16
LANG: PYTHON3
PROB: transform
"""

a=open('transform.in','r')
b=open('transform.out','w')

n=int(a.readline())

arr1=[]
for i in range(n):
    arr1.append(list(a.readline().strip()))
arr2=[]
for i in range(n):
    arr2.append(list(a.readline().strip()))


def rotate(l):
    ans=[]
    for i in range(n):
        thing=[]
        for i in range(n):
            thing.append(0)
        ans.append(thing)
    for i in range(n):
        for j in range(n):
            ans[j][n-i-1]=l[i][j]
    return ans

def flip(l):
    for i in range(n):
        l[i]=l[i][::-1]
        
def solve(arr1,arr2):
    arr1=rotate(arr1)
    if arr1==arr2:
        return 1
    arr1=rotate(arr1)
    if arr1==arr2:
        return 2
    arr1=rotate(arr1)
    if arr1==arr2:
        return 3
    arr1=rotate(arr1)
    flip(arr1)
    if arr1==arr2:
        return 4
    arr1=rotate(arr1)
    if arr1==arr2:
        return 5
    arr1=rotate(arr1)
    if arr1==arr2:
        return 5
    arr1=rotate(arr1)
    if arr1==arr2:
        return 5
    arr1=rotate(arr1)
    flip(arr1)
    
    
    if arr1==arr2:
        return 6
    return 7

b.write(str(solve(arr1,arr2))+'\n')
a.close()
b.close()


    
    
    
    
    
    
    
    
