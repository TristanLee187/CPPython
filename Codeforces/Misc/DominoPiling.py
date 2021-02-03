nums = input().split(' ')
M = int(nums[0])
N=int(nums[1])

if (N*M)%2==0:
    print(int(N*M/2))
else:
    print(int((N-1)*(M-1)/2 + int(M/2) + int(N/2)))
    
    
