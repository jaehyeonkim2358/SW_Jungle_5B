from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0

for i in range(2, N+1):
    if i in stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],
        dp[i-v][v],dp[i-v][v+1]) +1
        
ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)