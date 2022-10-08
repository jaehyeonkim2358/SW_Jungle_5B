import sys
sys.setrecursionlimit(15000)

n, m, k, x = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)

INF = 9999999999999
distance = [INF for _ in range(n+1)]
distance[x] = 0
def solution(start, dist):
    for next in edges[start]:
        if distance[next] > distance[start] + dist:
            distance[next] = distance[start] + dist
            solution(next, dist)

solution(x, 1)

flag = True
for i in range(len(distance)):
    if distance[i] == k:
        flag = False
        sys.stdout.write(f'{i}\n')

if flag:
    print('-1')