import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

dp = {i: 0 for i in range(1, n+1)}
dp[1] = 1
if n >= 2:
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746


print(dp[n])
