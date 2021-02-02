h,n=map(int,input().split(' '))
moves=[]
for i in range(n):
    moves.append(list(map(int, input().split(' '))))


dp=(h+1)*[float('inf')]
dp[0]=0
          

for i in range(1,h+1):
    for j in range(n):
        dp[i]=min(dp[i], dp[max(0, i-moves[j][0])]+moves[j][1])

print(dp[h])
                  
