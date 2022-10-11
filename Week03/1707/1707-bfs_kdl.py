import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 51732kb / 1620ms
K = int(input())


def bfs(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                if visited[node] == 'red':
                    visited[i] = 'blue'
                else:
                    visited[i] = 'red'
                queue.append(i)
            elif visited[node] == visited[i]:
                return False
    return True


for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visited = {i: 0 for i in range(1, V+1)}

    for _ in range(E):
        sv, ev = map(int, input().split())
        graph[sv].append(ev)
        graph[ev].append(sv)

    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 'red'
            res = bfs(i)
            if not res:
                break

    print('YES') if res is True else print('NO')
