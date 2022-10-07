import sys

n, m = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    edges[n1].append(n2)
    edges[n2].append(n1)


def solution(start):
    visited[start] = 1
    queue = [start]

    while queue:
        cur = queue.pop(0)
        for next in edges[cur]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1



visited = [0] * (n+1)
cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        solution(i)
        cnt += 1

print(cnt)