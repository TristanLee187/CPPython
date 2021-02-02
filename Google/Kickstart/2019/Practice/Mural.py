import functools

ans = ''
tests = int(input())
count = 0

def SUM(x):
    ans = 0
    for i in x:
        ans += int(i)
    return ans

while count<tests:
    n = int(input())
    vals = input()
    half = (len(vals))/2 + len(vals)%2
    point1 = int(0)
    point2 = int(half)
    Sum = 0
    while point1<half:
        l = list(vals[point1:point2])
        testsum = SUM(l)
        Sum = max(Sum,testsum)
        point1 += 1
        point2 += 1

    ans += 'Case #' + str(count+1) + ': ' + str(Sum) + '\n'
    count += 1

print(ans, end='')

        
        
