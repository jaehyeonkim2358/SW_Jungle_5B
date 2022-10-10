from collections import deque
import sys
sys.stdin = open("W03-W04/Week03/1260/input.txt","r")

n, m, start = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    if w not in adj[u]:
        adj[u].append(w)
        adj[w].append(u)

for l in adj:
    l.sort()
    
def DFS(adj, visited, v):
    visited[v] = True   # 인자로 받은 아이는 일단 방문한 것.
    print(v, end=' ')
    for w in adj[v]:
        if not visited[w]:
            DFS(adj, visited, w)

q = deque()
def BFS(adj, visited, v):
    visited[v] = True   # 처음 시작점은 방문한 것
    print(v, end=' ')
    while True:
        for w in adj[v]:
            if not visited[w]:
                q.append(w); visited[w]=True; print(w, end=' ')
        
        if not q : break
        v = q.popleft()

        
visited = [None] * (n+1)
DFS(adj, visited, start)

print()

visited = [None] * (n+1)
BFS(adj, visited, start)