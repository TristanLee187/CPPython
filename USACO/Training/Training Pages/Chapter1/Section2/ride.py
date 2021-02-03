"""
ID: tristan16
LANG: PYTHON3
PROG: ride
"""

a=open('ride.in', 'r')
b=open('ride.out', 'w')

s1=a.readline()[:-1]
s2=a.readline()[:-1]

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x)
    else: 
        # Element is not present in the array 
        return -1

def letterToNum(x):
    return binarySearch(letters, 0, 25, x)

first=1
for i in s1:
    first *= letterToNum(i)+1
second=1
for i in s2:
    second *= letterToNum(i)+1

ans=first%47==second%47
if ans:
    b.write('GO'+'\n')
else:
    b.write('STAY'+'\n')
    
    
