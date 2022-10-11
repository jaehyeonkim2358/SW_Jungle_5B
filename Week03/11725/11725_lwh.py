import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
sys.stdin = open('11725/11725_lwh.txt', 'r')
input = sys.stdin.readline

def dfs(nodes, u, parent):
    for v in nodes[u]:
        if not parent[v]:
            parent[v] = u
            dfs(nodes, v, parent)

def init():
    N = int(input())
    nodes = defaultdict(list)
    parent = [False] * (N+1)
    for _ in range(N-1):
        u, v = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    dfs(nodes, 1, parent)
    for p in parent[2:]:
        print(p)

init()