import sys
import heapq
from collections import deque, defaultdict
sys.stdin = open('18352/18352_lwh.txt', 'r')
input = sys.stdin.readline

def bfs(graph, start, costs):
    queue = []
    # (해당 노드까지의 최단거리, 노드번호) 튜플로
    heapq.heappush(queue, (0, start))
    costs[start] = 0

    ans = []

    while queue:
        dist, u = heapq.heappop(queue)
        
        if costs[u] == K:
            ans.append(str(u))
            continue
        
        for v in graph[u]:
            # 이때 costs[v] > dist 로 하면 안된다 frontier 끼리 인접일 경우 dist+1이 최소이어야할 애가 dist+2로 되버리는 case 발생
            if costs[v] > dist + 1:
                costs[v] = dist + 1
                heapq.heappush(queue, (costs[v], v))
    if ans:
        print('\n'.join(ans))
    else:
        print(-1)

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
costs = [N] * (N + 1)
for _ in range(M):
    edge = list(map(int, input().split()))
    u, v = edge[0], edge[1]
    graph[u].append(v)

bfs(graph, X, costs)
