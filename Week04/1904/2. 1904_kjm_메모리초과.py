# https://www.acmicpc.net/problem/1904
# https://kils-log-of-develop.tistory.com/244 정리 굿
import sys
input = sys.stdin.readline
n = int(input())

# dp = [0]* (n+1) #런타임 에러 뜬 원인(N) N이 백만까지니까 딱 백만만 넣으면 안되고 좀 넉넉히 넣어줘야함.
dp = [0]* (10000100)
dp[1] = 1
dp[2] = 2
# dp[3] = 3 
# dp[4] = 5
# dp[5] = 8
# 설마 피보나치? #이렇게 귀납적으로 넣어보면서 패턴을 찾는 것도 방법임
for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1])%15746
print(dp[n])



