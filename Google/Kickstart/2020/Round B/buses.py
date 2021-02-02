tests = int(input())
count = 0
while count<tests:
    nd = input().split(' ')
    N = int(nd[0])
    D = int(nd[1])
    times = input().split(' ')
    times = times[::-1]
    for i in times:
        D -= D%int(i)
    print('Case #' + str(count + 1) + ': ' + str(D))
    count += 1
