from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.stdin = open("W03-W04/Week03/1916/input.txt","r")

# init
n = int(input()) ; m = int(input())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
for _ in range(m):
    u, w, d= map(int, sys.stdin.readline().split())
    adj[u][w] = min(adj[u][w],d) # lesson 그래프에서 defaultdict > defaultdict > 숫자로 사용할 때 중복된 간선이 가중치만 다르게 들어온다면 가장 마지막에 들어온 가중치가 남게된다.
start, end = map(int, input().split())

distance = [float('inf')] * (n+1)
distance[start] = 0
distance_heap = []     #(dist, v )
heappush(distance_heap, (0, start))
# end of init

# distance 배열에는 시작 정점에서 각 정점(Index)까지의 최단경로 추정값이 저장되어있고,
# '현재까지 갱신된 정점(v)의 최단경로 추정값'이
# '직전원소(u)의 최단경로 추정값'과 '두 정점을 잇는 간선(u, v)의 가중치(w)' 합보다 큰 경우 이를 갱신시켜 준다.
# 
# distance 배열은 항상 distance에 대한 최신 정보를 가지고 있다.
# heap을 따로 쓰는 이유는 distance 배열을 선형탐색해 최소값을 찾는 번거러움을 덜기 위해.
# 그래서 distance_heap은 distance 배열의 최신 정보를 가지면서도, 이전 단계의 distance정보도 남아 있을 수 있다.
# 그래서 a에서 최신의 정보인지 확인을 해준다. distance는 생각해보면 줄어들면 줄어들었지 늘진 않는다. (항상 최소값으로 갱신하려고 함.)
# 따라서 distance_heap에서 꺼낸 v에 대한 dist정보가, distance배열의 해당 값보다 '크다면' 이미 이전 단계의 정보인 (visited된) 것이다.
# 그래서 continue를 통해 heap의 다음 최소값으로 넘어간다.
while distance_heap:
    dist, v = heappop(distance_heap)
    if distance[v] < dist:        # (a) visited check.
        continue
    # visited check를 통과한 정보의 v는 최신의 distance정보(Y 에서 다른 정점의 거리)에서 최소값을 가진 정점이다.
    # 이제 v는 Y에 들어온 것이다.
    
    # if v == end :    # 문제의 정답을 위한 코드. end값에 대한 최종 distance가 계산되었다면 그 값을 출력하고 종료한다.
    #     print(distance[v])
    #     break
    
    # v가 Y에 들어왔다는 사실은 아래에서 v에 대한 인접 정점들의 distance를 갱신해준다는 점에서 다시 한 번 알 수 있다.
    for w,d in adj[v].items():
        if distance[v]+d < distance[w]:
            distance[w] = distance[v]+d
            heappush(distance_heap, (d, w))
            
print(distance[end])

# Prim 과의 차이점은 exercise/Prim_vs_Dijkstra.jpg 참고.