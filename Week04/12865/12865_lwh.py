import sys
sys.stdin = open('Week04/12865/12865_lwh.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]

things = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    things.append((W, V))

for i in range(1, N + 1):
    W, V = things[i][0], things[i][1]
    for j in range(1, K + 1):
        if W > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(dp[N][K])