import sys
from collections import deque
# 큐를 구현하기 위해 deque을 사용한다.
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {num: [] for num in range(1, N+1)}
# 각 vertex의 연결을 파악하기 위해 dict 형태로 입력값을 받아준다.
for _ in range(M):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)
    # 입력값들을 통해 vertex들의 연결 상태를 받아준다.
for i in graph:
    graph[i].sort()


def dfs(node):
    if node in dfs_visited:
        return
    dfs_visited.append(node)
    for i in graph[node]:
        dfs(i)
    # node가  방문한적이 없으면 추가


def bfs(graph):
    visited = []
    # 사이클을 방지하기 위해 vertex의 연결 여부를 확인한다.
    # 추가로 노드의 연결 여부도 확인한다.
    # x in s 작업을 수행할 때 list 형식은 O(n)의 평균 속도를 갖지만. set 형식의 경우 평균 O(1)의 속도를 가진다.

    queue = deque()
    # 먼저 들어간 값을 먼저 pop을 시켜주어야 한다.
    # 스택으로 구현을 하게 될 경우 pop(0)을 하여야 하는데 이럴 경우 시간 복잡도가 O(n)이다.
    # deque는 linked list형식의 자료 구조로 배열의 양 끝에 접근이 가능하다.
    # popleft를 사용할 경우 pop(0)과 동일한 결과를 보이면서 시간복잡도는 O(1)이다.

    queue.append(V)
    # 시작 노드를 queue에 넣어준다.

    while queue:
        node = queue.popleft()
        # 인접한 노드부터 탐색하기 위해 (BFS)
        if node not in visited:
            # 방문한 노드을 또 가면 사이클, 방문 여부 확인
            visited.append(node)
            # 방문했으므로 추가
            queue.extend(graph[node])
            # 연결된 vertex들을 추가
            # appned를 쓸경우 TypeError: unhashable type: 'list'오류가 발생. para로 받은 ele 그대로의 값을 삽입하기 때문.
            # [2,3,4] 의 형태가 그대로 pop됨.
            # extend를 쓸 경우 iterable한 모든 ele를 넣음. deque([2, 3, 4])의 형태 2,3,4 하나씩 pop됨


dfs_visited = []
dfs(V)
print(*dfs_visited)
print(*bfs(graph))

# 모든 노드를 방문하고자 하는 경우에는 DFS를 가까운 노드부터 탐색하기 위해서는 BFS를 사용한다.
# 검색 속도 자체는 BFS가 빠르지만 DFS가 더 간단하다.
# 검색 대상 그래프가 크거나 경로의 특징을 저장해둬야 하는 문제는 DFS를,
# 검색 대상의 규모가 크지 않고 최단거리를 구해야 하는 문제는 BFS가 유리하다.
