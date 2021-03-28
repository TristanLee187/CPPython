n=int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
b = 2*b

c = 2*n*[0]


for i in range(n):
    for j in range(i, n+i):
        if a[i] == b[j]:
            c[j-i]+=1
            break
        

print(max(c))
    

    

    
