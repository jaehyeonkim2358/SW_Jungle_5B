import sys
from heapq import heappop, heappush


class Bus:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# initialize:
# 시작 정점에서 다른 모든 정점에 대한 최단경로 추정값을 무한대(도달 하지 못한 경우)로 초기화 하고
# 시작 정점 -> 시작 정점 경로의 최단경로 추정값은 0으로 초기화
def initialize_single_source(start):
    global INF, n
    distance = [INF] * (n+1)
    distance[start] = 0
    return distance

# relaxation: 현재까지 발견된 최단 경로의 개선 여부를 검사하고, 개선 가능하다면 이를 감소된 값으로 갱신하는 과정.
# distance 리스트에는 시작 정점에서 각 정점(Index)까지의 최단경로 추정값이 저장되어있고,
# '현재까지 갱신된 정점(v)의 최단경로 추정값'이 
# '직전원소(u)의 최단경로 추정값'과 '두 정점을 잇는 간선(u, v)의 가중치(w)' 합보다 큰 경우 이를 갱신시켜 준다.
def relax(distance, u, v, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        return True
    return False


# single-source(단일 출발지) 문제의 해결 방법인 dijkstra를 single-pair(단일 쌍) 문제 해결에도 사용할 수 있다.
def dijkstra(start, end):
    distance = initialize_single_source(start)
    min_heap = []
    heappush(min_heap, Bus(start, 0))
    while min_heap:
        current_bus = heappop(min_heap)
        # 현재 순회중인 정점에 대해, 시작 정점에서의 최단경로 추정값 보다 큰 가중치를 가진 간선이라면 이용하지 않음
        if distance[current_bus.dest] < current_bus.cost:
            continue
        for next_bus in bus[current_bus.dest]:
            if relax(distance, current_bus.dest, next_bus.dest, next_bus.cost):
                heappush(min_heap, next_bus)
    return distance[end]


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    bus[u].append(Bus(v, c))

start, end = map(int, sys.stdin.readline().split())
INF = 999999999999999
total_cost = [INF] * (n+1)

answer = dijkstra(start, end)
print(answer)
