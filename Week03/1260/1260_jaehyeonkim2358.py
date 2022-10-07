import sys

n, m, v = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[1] not in edges[tmp[0]]:
        edges[tmp[0]].append(tmp[1])
        edges[tmp[1]].append(tmp[0])


for edge in edges:
    edge.sort()


def dfs(start):
    visited[start] = 1
    sys.stdout.write(f'{start} ')
    for e in edges[start]:
        if visited[e] == 0:
            dfs(e)


def bfs(start):
    pqueue = []
    path_2 = f'{start} '
    pqueue.append(start)
    visited[start] = 1

    while pqueue:
        cur = pqueue.pop(0)
        for next in edges[cur]:
            if visited[next] == 0:
                pqueue.append(next)
                visited[next] = 1
                path_2 += f'{next} '
    print(path_2)


visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)
