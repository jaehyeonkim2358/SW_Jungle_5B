import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
sys.stdin = open('11724/11724_lwh.txt', 'r')
input = sys.stdin.readline

def dfs(V):
    if not visited[V]:
        visited[V] = True
        for i  in edges[V]:
            dfs(i)
        return True
    return False

N, M = map(int, input().split())
edges = defaultdict(list)
count = 0
for _ in range(M):
    edge = list(map(int, input().split()))
    u, v = edge[0], edge[1]
    edges[u].append(v)
    edges[v].append(u)

visited = [False] * (N + 1)
for idx in range(1, N+1):
    if dfs(idx) == True:
        count += 1
print(count)