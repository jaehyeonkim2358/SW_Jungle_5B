import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
# dp테이블 초기화
if n == 1:
    dp[1] = 1
if n == 2:
    dp[1] = dp[2] = 1

if n > 2:
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    # 밑에서부터 n까지 반복해서 올라감

print(dp[n])
