<<<<<<< HEAD
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = []
    for i in s:
        l.append(int(i))
    from math import ceil

    ans = sum(l[:ceil(n / 2)])
    curr = ans
    for i in range(ceil(n / 2), n):
        curr -= l[i - ceil(n / 2)]
        curr += l[i]
        ans = max(ans, curr)

    print('Case #' + str(_ + 1) + ': ' + str(ans))

=======
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

        
        
>>>>>>> af72bacd08f89b126d6c7a2536f223afad5a058f
