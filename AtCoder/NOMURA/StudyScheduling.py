l=list(map(int, input().split(' ')))
start = l[0]*60+l[1]
end = l[2]*60+l[3]
print(end-start-l[4])
