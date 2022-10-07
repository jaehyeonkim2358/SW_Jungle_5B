import sys, heapq


class Edge:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return f'dest: {self.dest}, cost: {self.cost}'


INF = 9999999999999

v, e = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(v+1)]
for _ in range(e):
    n1, n2, cost = map(int, sys.stdin.readline().split())
    edges[n1].append(Edge(n2, cost))
    edges[n2].append(Edge(n1, cost))


def add_edge(queue, vertex):
    for e in edges[vertex]:
        heapq.heappush(queue, e)
    
    
def prim(root):
    global INF

    total_cost = 0          # MST의 가중치 합을 저장할 변수

    visited = [0] * (v+1)   # 정점이 연결되었는지 여부를 체크해줄 리스트
    queue = []              # 간선의 가중치를 key로 하는 min_heap으로 이용할 리스트

    # 최초 시작 위치(root)는 가중치가 0인 간선으로 저장해준다.
    heapq.heappush(queue, Edge(root, 0))

    # 모든 정점의 수 만큼 반복한다.
    for _ in range(v):
        cur_node = -1
        min_cost = INF
        while queue:
            tmp = heapq.heappop(queue)
            cur_node = tmp.dest
            if visited[cur_node] == 0:
                min_cost = tmp.cost
                break

        # 모든 정점의 수-1 만큼 간선을 연결하기 전에 최소 비용이 갱신되지 않았다는 뜻은
        # queue가 가지고 있는 간선으로 연결할 수 있는 새로운 정점이 더 이상 존재하지 않는다는 이야기이며,
        # 이는 곧 그래프 내의 모든 정점이 서로 '도달 가능한 상태'가 될 수 없음을 의미한다.
        # 따라서 최소 신장 트리(MST)를 만들 수 없기 때문에, 조건에서 가중치의 합으로 나올 수 없는 수를 return 시켜준다.
        if min_cost == INF:
            return INF

        # 현재 연결한 간선의 가중치값을 더해줌
        total_cost += min_cost

        # 현재 순회에서 방문한 정점에 대한 방문 체크
        visited[cur_node] = 1

        # 현재 순회에서 방문한 정점으로 연결할 수 있는 새로운 간선을 queue에 담아온다.
        add_edge(queue, cur_node)
        
    return total_cost


print(prim(1))