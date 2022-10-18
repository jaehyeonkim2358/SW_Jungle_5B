# 외판원 순회
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**8)

N = int(input())
graph = []
for _ in range(N):
    graph.append(tuple(map(int, input().split(' '))))

dp = [[-1]*(1<<N) for _ in range(N)]

def dfs(x, visit):
    if dp[x][visit] != -1:
        return dp[x][visit]

    if visit == (1<<N)-1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return sys.maxsize

    min_cost = sys.maxsize
    for i in range(1, N):
        if graph[x][i] == 0:
            continue
        if visit & (1<<i):
            continue
        tmp = dfs(i, visit|(1<<i))+ graph[x][i]
        if tmp < min_cost:
            min_cost = tmp
    dp[x][visit] = min_cost
    return min_cost

print(f'{dfs(0, 1)}')