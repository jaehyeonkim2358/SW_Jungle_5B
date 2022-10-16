# https://www.acmicpc.net/problem/9084
# https://d-cron.tistory.com/23 설명 굿

# 입력
import sys
input = sys.stdin.readline
T = int(input()) #test회수
for i in range(T):
  N = int(input()) #동전 가지 수 
  coins = list(map(int, input().split()))
  coins.insert(0,0)
  M = int(input()) #동전으로 만들어야하는 금액 
  # print(coins)
  
  dp = [[0]*(M+1) for i in range(N+1)]
  # 모든 동전들의 0을 만드는 방법은 1이다 (안 내버리면 됨)
  for i in range(N+1):
    dp[i][0] = 1
  
  for r in range(1, N+1):
    for c in range(1,M+1):
      dp[r][c] = dp[r-1][c] #무슨의도인지?
      if c -coins[r]>= 0:  #현재 인덱스에 지금 보고있는 동전 금액을 빼버린다.
        #i는 8, coins[j]는 4 (j는 2)
        dp[r][c] = dp[r][c] +dp[r][c-coins[r]] 
  print(dp[N][M])
