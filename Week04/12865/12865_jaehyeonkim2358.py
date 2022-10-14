# Knapsack
import sys


n, k = map(int, sys.stdin.readline().split())
knapsack = [0]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    if w <= k:
        knapsack.append((w, v))

dp = [0] * (k+1)
for item in knapsack:
    weight, value = item
    for j in range(k, weight-1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

sys.stdout.write(f'{dp[k]}')