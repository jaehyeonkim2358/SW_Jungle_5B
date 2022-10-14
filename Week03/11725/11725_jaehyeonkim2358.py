import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    edges[vertex1].append(vertex2)
    edges[vertex2].append(vertex1)

parent = [-1] * (n+1)

def find_parent(root):
    global n
    queue = deque([root])
    parent[root] = 1
    cnt = 0
    while queue:
        cur = queue.popleft()
        if cnt == n:
            return
        for child in edges[cur]:
            if parent[child] == -1:
                cnt += 1
                parent[child] = cur
                queue.append(child)

find_parent(1)
for i in range(2, n+1):
    sys.stdout.write(f'{parent[i]}\n')