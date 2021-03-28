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

l=list(map(int, input().split(' ')))

find=l[0]
n=l[1]

if n==0:
    print(find)
else:
    l=list(map(int, input().split(' ')))
    l=sorted(l)

    a=find
    b=find
    
    while True:
        if binarySearch(l, 0, n-1, b)==-1:
            print(b)
            break
        elif binarySearch(l, 0, n-1, a)==-1:
            print(a)
            break
        else:
            a+=1
            b-=1
        


