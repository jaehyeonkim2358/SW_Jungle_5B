import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = {i: []for i in range(1, N + 1)}
visited = set()
answer = {i: 0 for i in range(1, N+1)}
for _ in range(N-1):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)

for i in graph:
    graph[i].sort()


def bfs(node):
    visited = set()
    queue = deque()
    queue.append(node)

    # while queue:
