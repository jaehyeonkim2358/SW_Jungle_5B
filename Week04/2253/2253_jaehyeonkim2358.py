from math import sqrt
import sys

n, m = map(int, sys.stdin.readline().split())

trap = set(int(sys.stdin.readline().rstrip()) for _ in range(m))

INF = float('inf')
max_v = int(2*(n**.5)) + 2
dp = [[INF] * (max_v) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in trap:
        continue
    for v in range(1, int(2*(i**.5))+1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

ans = min(dp[n])
if ans == INF:
    ans = -1
sys.stdout.write(f'{ans}')