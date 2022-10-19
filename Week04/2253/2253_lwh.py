import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
sys.stdin = open('Week04/2253/2253_lwh.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())

INF = 10000
# dp = [[0]*(N+1) for _ in range(N+1)]
dp = defaultdict(set)
holes = set([int(input()) for _ in range(M)])
def jump(u, x):
    # if dp[u][x]:
        # return dp[u][x]
    if dp[(u, x)]:
        return dp[(u, x)]

    if u in holes: # 못 가는 돌 밟으면
        return INF

    if u == N:  # 목적지 도착
        return 0

    min_jump = INF
    if x - 1 and u + x - 1 <= N:
        min_jump = min(min_jump, jump(u + x - 1, x-1) + 1)
    if u + x <= N:
        min_jump = min(min_jump, jump(u + x, x) + 1)
    if u + x + 1 <= N:
        min_jump = min(min_jump, jump(u + x + 1, x + 1) + 1)

    # dp[u][x] = min_jump
    dp[(u, x)] = min_jump
    return min_jump

ans = jump(2, 1) + 1
if ans >= INF:
    print(-1)
else:
    print(ans)