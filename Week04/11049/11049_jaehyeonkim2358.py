import sys

n = int(sys.stdin.readline().rstrip())
matrix = [0] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
INF = 2**31
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n-i+1):
        _from = j
        _to = i+j
        dp[_from][_to] = INF
        for k in range(_from, _to):
            dp[_from][_to] = min(dp[_from][_to], dp[_from][k] + dp[k+1][_to] + matrix[_from][0] * matrix[k][1] * matrix[_to][1])

sys.stdout.write(f'{dp[1][n]}')