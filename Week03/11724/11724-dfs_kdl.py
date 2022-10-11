import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)

dfs_visited = set()


def dfs(node):
    if node in dfs_visited:
        return
    dfs_visited.add(node)
    for i in graph[node]:
        dfs(i)


ans = 0
for i in range(1, N + 1):
    if i not in dfs_visited:
        dfs(i)
        ans += 1

print(ans)
