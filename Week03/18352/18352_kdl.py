import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    start_city, end_city = map(int, input().split())
    graph[start_city].append(end_city)

how_far = {i: 'no' for i in range(1, N+1)}  # 방문 여부 및 최단 거리 확인 목적
ans = []


def bfs(x):
    queue = deque([x])  # 탐색을 위한 queue 생성
    how_far[x] = 0  # 맨 처음 시작하는 도시의 거리는 당연히 0 (방문처리 + 거리 부여)
    while queue:  # 모든 도시를 다 확인할 때까지
        city = queue.popleft()
        # 시티를 꺼내서 확인을 한다.
        for next_city in graph[city]:  # 시티의 인접 노드를 확인
            if how_far[next_city] == 'no':  # 방문 여부 확인
                how_far[next_city] = how_far[city] + 1
                # 방문 안했으면 인접 도시보다 1만큼의 거리가 있으므로 1추가
                queue.append(next_city)
                # 다음 도시들도 확인하기 위해 queue에 appned
                # extend(graph[next_city])를 사용하게 되면 graph[2] >> 3,4가 append됨 >> 그래프 실행이 안됨.
                # append(next_city)를 사용하게 되면 2,3이 append됨
                # 그러면 2와 연결된 도시들도 하나씩 count할 수 있게됨.
    for i in range(1, N+1):
        if how_far[i] == K:  # 최단 거리와 일치하는 도시찾기.
            ans.append(i)


bfs(X)
if not ans:
    print(-1)
else:
    for i in range(len(ans)):
        print(ans[i])
