import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)


def bfs(s_node):
    queue = deque()
    queue.append(s_node)

    while queue:
        node = queue.popleft()
        if node not in bfs_visited:
            bfs_visited.add(node)
            queue.extend(graph[node])


bfs_visited = set()
ans = 0

for i in range(1, N+1):
    if i not in bfs_visited:
        bfs(i)
        ans += 1

print(ans)
