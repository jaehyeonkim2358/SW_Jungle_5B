import sys
from collections import deque, defaultdict
sys.stdin = open('1707/1707_lwh.txt', 'r')
input = sys.stdin.readline

def bfs(graph, u, group):
    q = deque([u])
    group[u] = 1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if group[v] == group[u]:
                return False # -> NO
            elif group[v]:
                continue
            elif not group[v]:
                group[v] = -group[u]
                q.append(v)
    return True
        
def init():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    group = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for node in graph.keys():
        if group[node]: # 아지 안 간 그룹인지 확인
            continue 
        if not bfs(graph, node, group):
            print('NO')
            return
    print('YES')

K = int(input())
for _ in range(K):
    init()

