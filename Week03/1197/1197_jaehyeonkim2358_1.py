import sys

# Edge: 간선을 이루는 두 정점과 가중치를 가지는 class
class Edge:
    # 초기화 메서드(생성자). 매개변수는 순서대로 정점1, 정점2, 가중치
    def __init__(self, n1, n2, cost):
        self.n1 = n1
        self.n2 = n2
        self.cost = cost

    # (less then). 객체간 비교를 위한 메서드. 가중치의 오름차순으로 객체를 정렬하기 위해 사용
    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self) -> str:
        return 'n1: {}, n2: {}, cost: {}'.format(self.n1, self.n2, self.cost)


# union(): 두 노드를 각각 포함하는 트리를 합쳐준다.
# 두 트리가 합쳐지면 두 정점 사이의 이동 가능한 경로가 존재함
def union(a, b):
    a = find(a)
    b = find(b)
    # a, b의 root가 같으면 합칠 필요 없음
    if a == b:
        return

    # a, b의 root가 다른 경우, 트리의 높이(rank)가 더 낮은 트리를 높은 트리 밑에 넣는다.
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a

    if rank[a] == rank[b]:
        rank[a] += 1


# find(): 노드를 포함하는 트리의 root 노드를 찾는다.
def find(x):
    # 자기 자신이 root 노드일 경우 그대로 return
    if x == parent[x]:
        return x
    # 그 외의 경우 재귀 호출을 통해 부모노드의 부모를 찾는다.
    else:
        # 이때, 찾은 x가 속한 트리의 root 노드를 x의 부모 노드로 바로 연결시켜주며 트리를 압축한다.
        parent[x] = find(parent[x])
        return parent[x]


v, e = map(int, sys.stdin.readline().split())
edges = []

for _ in range(e):
    n1, n2, cost = map(int, sys.stdin.readline().split())
    edges.append(Edge(n1, n2, cost))

# parent : index의 부모노드를 저장하는 리스트
# 처음에 각 노드 자기 자신을 root로 초기화
parent = [i for i in range(v+1)]

# rank: index의 트리 길이를 저장하는 리스트
# 트리의 길이를 비교해서 효율적으로 압축하기위해 사용한다.
# 자신이 root인 각 노드의 길이는 0
rank = [0] * (v+1)

# 입력받은 간선을 가중치의 가중치가 감소하지 않는 순서(오름차순)으로 순회하기 위해 정렬한다
edges.sort()

total = 0   # 최소 비용을 저장할 변수
for edge in edges:
    # 두 정점의 root가 같지 않을 경우에만 union()을 진행하며 cost를 계산해준다.
    # 그 이유는 순회 순서가 가중치의 오름차순 이므로, 두 정점이 사이의 경로가 존재하는 상태 인 경우, 이미 최소 비용으로 연결 되어있기 때문.
    if find(edge.n1) != find(edge.n2):
        union(edge.n1, edge.n2)
        total += edge.cost

print(f'{total}')
