import sys
from collections import deque, defaultdict
sys.stdin = open('18352/18352_lwh.txt', 'r')
input = sys.stdin.readline

def bfs(graph, start, costs, visited):
    queue = deque([start])
    costs[start] = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                costs[i] = costs[v] + 1
                visited[i] = True
                queue.append(i)
    flag = False    
    for idx, cost in enumerate(costs):
        if cost == K:
            print(idx)
            flag = True
    if flag == False:
        print(-1)

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
costs = [-1] * (N + 1)
visited = [False] * (N + 1)
for _ in range(M):
    edge = list(map(int, input().split()))
    u, v = edge[0], edge[1]
    graph[u].append(v)

bfs(graph, X, costs, visited)

# 개선 요소 1 : X에서 거리 K 까지 탐색완료 시 탐색 종료 하도록 수정
# 개선 요소 2 : 거리 K 인 도시목록 오름 차순 출력을 위한 정렬을 heap을 사용하면 time 이득
# 개선 요소 3 : 처음 초기화 시 cost = sys.maxsize 혹은 문제 조건 최대값 이상으로 초기화 하여 
# 탐색 중인 cost 보다 큰 값을 갖고 있다면 방문 안했다는 지표로 사용 가능
# -> visited 배열을 따로 관리하지 않아도 됨