
ans = ''
tests = int(input())
count = 0

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

while count<tests:
    inp = input()
    N = int(inp[0])
    P = int(inp[2])
    skills = input().split(' ')
    skillz = []
    for i in skills:
        skillz += [int(i)]

    mergeSort(skillz)
    print(skillz)
    diffs = []
    for i in list(range(N-1)):
        diffs += [skillz[i+1] - skillz[i]]
    mergeSort(diffs)
    print(diffs)
    Sum = 0
    times = 1
    for i in diffs:
        if i!=0:
            Sum += i*times
            times += 1
        if times==P:
            break
    ans += 'Case #' + str(count+1) + ': ' + str(Sum) + '\n'
    count += 1

print(ans)
    
    
    
    

