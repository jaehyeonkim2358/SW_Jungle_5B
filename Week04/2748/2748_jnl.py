# 피보나치 수 2
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
dp = [-1 for _ in range(N+1)]

def fibo(n):
    for i in range(n+1):
        if i <= 1:
            dp[i] = i
            continue
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n+1]

print(f'{fibo(N)}')