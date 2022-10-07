import sys

n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(n+1)]
for _ in range(e):
    n1, n2 = map(int, sys.stdin.readline().split())
    edges[n1].append(n2)
    edges[n2].append(n1)


def solution(start):
    global n
    visited = [0] * (n+1)
    queue = [start]
    visited[start] = 1
    cnt = 0
    while queue:
        cur = queue.pop(0)
        for next in edges[cur]:
            if visited[next] == 0:
                cnt += 1
                queue.append(next)
                visited[next] = 1
    return cnt


print(solution(1))