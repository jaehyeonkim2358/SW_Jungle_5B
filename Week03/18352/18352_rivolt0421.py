from collections import defaultdict, deque
import sys
sys.stdin = open("W03-W04/Week03/18352/input.txt","r")

# init
n, m, k, start = map(int, input().split())
#  adj = defaultdict(set)
adj = defaultdict(list) # 리스트가 더 빠르다.
for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    adj[u].append(w)
visited = [False] * (n+1)
visited[start] = True
q = deque([start])
steps = -1
# end of init

while q:
    adj_cnt = len(q)
    steps += 1
    if steps == k:
        break
    
    while adj_cnt > 0:
        v = q.popleft()
        for w in adj[v]: 
            if not visited[w]:
                visited[w] = True
                q.append(w)
        adj_cnt -= 1

if q:        
    print(*sorted(q), sep='\n')     # 오름차순으로 출력해야 한다는 조건이 있다.
else:
    print(-1)