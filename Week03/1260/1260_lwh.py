import sys
from collections import deque
from collections import defaultdict
sys.stdin = open('1260/1260_lwh.txt', 'r')
input = sys.stdin.readline 

def solve_dfs(graph, v):
    visited = [False] * (N + 1)
    route = []
    def dfs(graph, v, visited):
        visited[v] = True
        route.append(v)
        for i in sorted(graph[v]):
            if not visited[i]:
                dfs(graph, i, visited)
    dfs(graph, V, visited)
    print(*route)

def solve_bfs(graph, start):
    visited = [False] * (N + 1)
    route = []
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            route.append(v)
            for i in sorted(graph[v]):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    bfs(graph, start, visited)
    print(*route)

N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = defaultdict(list)
for edge in edges:
    start, to = edge[0], edge[1]
    graph[start].append(to)
    graph[to].append(start)

solve_dfs(graph, V)
solve_bfs(graph, V)