import sys

n = int(sys.stdin.readline().rstrip())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

INF = float('inf')
dp = [[0] * (1 << n - 1) for _ in range(n)]
visited = 1

def solution(i, visited):
    if dp[i][visited] != 0:
        return dp[i][visited]

    if visited == (1 << n - 1) - 1:
        if W[i][0] != 0:
            return W[i][0]
        else:
            return INF

    min_dist = INF
    for j in range(1, n):
        if W[i][j] == 0:
            continue
        if visited & (1 << j - 1):
            continue

        dist = W[i][j] + solution(j, visited | (1 << j - 1))

        if min_dist > dist:
            min_dist = dist

    dp[i][visited] = min_dist
    return min_dist

print(solution(0, 0))