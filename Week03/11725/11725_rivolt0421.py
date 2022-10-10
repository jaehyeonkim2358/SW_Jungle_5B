from collections import defaultdict, deque
import sys
sys.stdin = open("W03-W04/Week03/11725/input.txt","r")

n = int(input())
adj = defaultdict(list)
parent = [0] * (n+1)
for _ in range(n-1):
    u, w = map(int, sys.stdin.readline().split())
    adj[u].append(w)
    adj[w].append(u)
    
stk = deque([1])
while stk:
    v = stk.pop()
    for w in adj[v]:
        if parent[w] == 0:
            parent[w] = v
            stk.append(w)

for x in parent[2:]:
    print(x)