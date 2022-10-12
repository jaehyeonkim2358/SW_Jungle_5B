import sys
from collections import defaultdict
from heapq import heappop, heappush
sys.setrecursionlimit(10**9)

class Edge:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = defaultdict(set)
r_graph = defaultdict(set)
in_degree = [0] * (n+1)
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    graph[u].add(Edge(v, d))
    r_graph[v].add(Edge(u, d))
    in_degree[v] += 1

start, end = map(int, sys.stdin.readline().split())

root = []
for id in range(1, n+1):
    if in_degree[id] == 0:
        root.append(Edge(id, 0))

INF = 999999999999999

count = 0
def init_distance(q):
    global INF
    distance = [0] * (n+1)

    while q:
        cur = heappop(q)
        for next in graph[cur.dest]:
            if distance[next.dest] < distance[cur.dest] + next.cost:
                distance[next.dest] = distance[cur.dest] + next.cost
            in_degree[next.dest] -= 1
            if in_degree[next.dest] == 0:
                heappush(q, next)
    return distance


def dfs(visited: list, distance: list, cur: Edge):
    global count
    if visited[cur.dest]:
        return
    visited[cur.dest] = True
    for next in r_graph[cur.dest]:
        if distance[cur.dest] == distance[next.dest] + next.cost:
            dfs(visited, distance, next)
            count += 1
    

def solution(end, root):
    global n, count
    
    distance = init_distance(root)

    visited = [False] * (n+1)

    count = 0
    dfs(visited, distance, Edge(end, 0))
    answer = max(distance)
    print(answer)
    print(count)


solution(end, root)