import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
# 각 vertex의 노드들은 자기 자신을 부모 노드로 가진다. 이를 위해 부모 노드를 할당한다.
graph = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph.append([start, end, weight])
    # 입력값읠 연결할 두 vertex와 해당 edge의 weight를 입력받는다.

graph = sorted(graph, key=lambda x: x[2])
# weight 기준으로 graph 정렬. krusckal 알고리즘을 사용하기 위해 오름차순으로 정렬한다.


def find_parent(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find_parent(parent[a])
        return parent[a]
    # 부모노드를 찾는다.


def union(a, b):
    a = parent[a]
    b = parent[b]
    if a < b:  # 작은 숫자가 부모노드가 된다.
        parent[b] = a
        # a가 b의 부모 노드가 된다.
    else:
        parent[a] = b
    # 노드를 결합한다.


ans = 0
for s, e, w in graph:
    sroot = find_parent(s)
    eroot = find_parent(e)
    # 연결될 vertex의 부모노드를 확인한다 > 사이클 여부 확인.
    if sroot != eroot:
        # start의 부모 노드와 end의 부모노드가 일치하지 않는다 = 두 노드를 연결해도 사이클이 발생하지 않는다.
        union(sroot, eroot)
        # 노드를 결합한다 > 이제 두 노드는 연결되었음.
        ans += w
        # edge가 연결되었으므로, 해당 edge의 가중치를 더한다.

print(ans)
