import sys
from heapq import *
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


INF = 100000000
N = int(input())  # 도시
M = int(input())  # 버스의 개수(edge)

# 도시에서 도시까지의 거리를 저장해줄 dict를 만든다.
distance = {i: INF for i in range(1, N+1)}

# 그래프 구현.
graph = defaultdict(list)

for _ in range(M):
    start_city, end_city, weight = map(int, input().split())
    graph[start_city].append((weight, end_city))

departure, arrival = map(int, input().split())


def dijkstra(start, end):

    p_queue = []  # 우선 순위 큐 생성
    heappush(p_queue, (0, start))
    distance[start] = 0  # 출발지에서 출발지로 가는 거리는 0
    while p_queue:  # 반복문 돌린다.
        weight, curr_dest = heappop(p_queue)
        # 기존의 거리와 다른 변수에서 해당 변수로 가는 거리가 더 작다면
        if distance[curr_dest] < weight:
            continue
        # 해당 경로가 더 짧으면 반복을 할 이유가 없음
        for next_w, next_d in graph[curr_dest]:
            new_w = weight + next_w  # 새로운 거리는 기존 거리 + 인접노드까지 거리
            if distance[next_d] > new_w:  # 새로운 거리가 더 짧은 거리라면
                heappush(p_queue, (new_w, next_d))  # 새로운 거리와 짧은 노드를 큐에 삽입.
                distance[next_d] = new_w
                # 새로운 거리로 교체한다.

    print(distance[end])


dijkstra(departure, arrival)
