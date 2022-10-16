import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    coins.insert(0, 0)
    M = int(sys.stdin.readline())

    dp = [[0] * (M+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1

    for j in range(1, N+1):
        for i in range(1, M+1):
            dp[j][i] = dp[j-1][i]
            if i-coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
    print(dp[N][M])