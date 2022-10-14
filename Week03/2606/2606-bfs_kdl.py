import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)

for i in graph:
    graph[i].sort()


def bfs(sn):
    visited = set()
    queue = deque()
    queue.append(sn)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return len(visited)-1


print(bfs(1))
