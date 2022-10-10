from collections import defaultdict, deque
import sys
sys.stdin = open("W03-W04/Week03/2606/input.txt","r")

n = int(input()); m = int(input())
adj = defaultdict(list)
visited = [0] * (n+1)

for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    adj[u].append(w)    
    adj[w].append(u)

stk = deque([1])
while stk:
    w = stk.pop()
    if not visited[w]:
        visited[w] = 1
        for u in adj[w]:
            if not visited[u]:
                stk.append(u)

print(sum(visited)-1)
