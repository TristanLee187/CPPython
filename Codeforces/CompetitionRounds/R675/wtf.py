def computeCost(arr, N, X):
    cost = 0
    for i in range(N):
        cost += abs(arr[i] - X)
    return cost


# Method to find minimum cost to
# make all elements equal
def minCostToMakeElementEqual(arr, N):
    low = high = arr[0]

    # Setting limits for ternary search
    # by smallest and largest element
    for i in range(N):

        if (low > arr[i]): low = arr[i]
        if (high < arr[i]): high = arr[i]

    # loop until difference between low and
    # high become less than 3, because after
    # that mid1 and mid2 will start repeating
    while ((high - low) > 2):

        # mid1 and mid2 are representative
        # array equal values of search space
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        cost1 = computeCost(arr, N, mid1)
        cost2 = computeCost(arr, N, mid2)

        # if mid2 point gives more total
        # cost, skip third part
        if (cost1 < cost2):
            high = mid2

        # if mid1 point gives more total
        # cost, skip first part
        else:
            low = mid1

    # computeCost gets optimum cost by
    # sending average of low and high as X
    return computeCost(arr, N, (low + high) // 2)

l=list(map(int,input().split()))
print(minCostToMakeElementEqual(l,len(l)))