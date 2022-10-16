# 01타일
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

def tile(n):
    if n == 1:
        return 1
    dp = [1 for _ in range(N+1)]
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 15746
    return dp[n]
print(f'{tile(N)}')