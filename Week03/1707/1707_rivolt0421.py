from collections import defaultdict, deque
import sys
sys.stdin = open("W03-W04/Week03/1707/input.txt","r")

def BFS(n, adj, color, start):
    for start in range(1,n+1):  # 연결 성분이 두개 이상인 그래프를 위해 모든 노드를 시작점으로 줘본다.
        if color[start] != 0 : continue # 대신 이미 colored(visited)된 노드는 바로 건너 뛴다.
        
        color[start] = 1
        q = deque([start])
        while True:
            v = q.popleft()
            for w in adj[v]:
                if color[w] == 0:
                    color[w] = -color[v]    # color를 주는 visited.
                    q.append(w)
                else: # 컬러 이미 지정되어 있는 경우
                    if color[w] == color[v]:
                       return 'NO'
                        
            if not q : break
    
    return 'YES'

k = int(input())
for i in range(k):
    # Test case
    # initializing
    n, m = map(int, input().split())
    adj = defaultdict(list)
    color = [0] * (n+1)
    for j in range(m):
        u, w = map(int, sys.stdin.readline().split())
        adj[u].append(w)
        adj[w].append(u)
    # end of initializing
    
    print(BFS(n, adj, color, 1))

