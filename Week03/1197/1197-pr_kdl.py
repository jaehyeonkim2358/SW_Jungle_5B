import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def prim():
    V, E = map(int, input().split())
    graph = [[]for _ in range(V+1)]
    total_min_weight = 0
    p_queue = []
    visited = [False] * (V+1)
    # V+1개를 만드는 이유는 인덱스의 값과 value의 값을 일치시키기 위함. [0]은 그냥 비워둠.
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append([weight, end])
        graph[end].append([weight, start])
    # 두 개의 정점이 서로 연결되어있음.
    # 1과 2가 연결되어 있다 그러면 1에서 시작하는 루트하나 2에서 시작하는 루트 하나가 추가 된 것.

    heappush(p_queue, [0, 1])

    while p_queue:
        dest = heappop(p_queue)
        # 목적지의 데이터를 가져오고 weight가 minumum인 edge를 얻기 위해 pop을 씀.
        if visited[dest[1]] == False:
            visited[dest[1]] = True
            # 방문을 하지 않았을 경우 방문하였다고 갱신.
            min_weight = dest[0]
            total_min_weight += min_weight
            # 방문을 안한 node가 나올 때까지 반복.
            for i in graph[dest[1]]:
                heappush(p_queue, i)
            # 다시 해당 목적지와 연결된 인접 vertex를 heap에 push해준다.
    return total_min_weight


print(prim())
