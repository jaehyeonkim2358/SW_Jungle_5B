import sys

n, m, k, x = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)

INF = 9999999999999

def solution(start):
    global k
    visited = [INF] * (n+1)
    visited[start] = 0

    queue = []
    queue.append(start)
    cnt = 0

    while queue:
        size = len(queue)
        cnt += 1
        if cnt > k:
            return visited
        while size > 0:
            cur = queue.pop(0)
            for next in edges[cur]:
                if visited[next] == INF:
                    visited[next] = cnt
                    queue.append(next)
            size -= 1

    return visited

distance = solution(x)
flag = True
for i in range(len(distance)):
    if distance[i] == k:
        flag = False
        sys.stdout.write(f'{i}\n')

if flag:
    print('-1')