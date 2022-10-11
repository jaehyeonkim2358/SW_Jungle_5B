import sys
from collections import defaultdict
sys.stdin = open('1707/1707_lwh.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, u, group):
    global flag
    for v in graph[u]:
        if group[v] == group[u]:
            flag = False
            return            
        elif group[v] == 0: # not visited
            group[v] = -group[u]
            dfs(graph, v, group)

def init():
    global flag
    flag = True

    V, E = map(int, input().split())
    graph = defaultdict(list)
    group = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for node in graph.keys():
        if group[node]:
            continue
        else:
            group[node] = 1
        dfs(graph, node, group)
        if not flag:
            print('NO')
            return
    print('YES')

flag = True
K = int(input())
for _ in range(K):
    init()