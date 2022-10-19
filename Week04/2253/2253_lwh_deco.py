import sys
import functools
sys.setrecursionlimit(10**5)
sys.stdin = open('Week04/2253/2253_lwh.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

INF = float('inf') # N + 1 이런 것 보다 그냥 상수로 초기화 해주는 게 훨! 씬! 빠! 름!
holes = set([int(input()) for _ in range(M)])

@functools.cache
def jump(u, x):
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

    return min_jump

ans = jump(2, 1) + 1
if ans >= INF:
    print(-1)
else:
    print(ans)