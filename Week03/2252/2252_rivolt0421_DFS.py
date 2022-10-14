from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("W03-W04/Week03/2252/input.txt","r")
# 위상정렬 : topology[탑 (이데)올로기] sort
#   DAG : Directed Acyclic Graph 를 대상으로 한다.
#
#   사이클에 포함된 원소들은 방문되지(= 큐에 들어가지 = DFS로 방문되지) 못한다.
#   맨처음 진입차수가 0인 정점들을 찾을 때도 제외되고, 시작 되고 나서도 그들의 진입차수를 0으로 만들수 없다. 서로 차수가 물려있기 때문에.
#   
#   오직 정점의 진입차수가 0이 되는 것에만 관심이 있다.
#   정점이 탐색되었어도, 정점의 진입차수가 0이 되지 않았다면 아직 방문할 수 없기 때문이다.
#
#   모든 원소가 방문되기 전에 큐가 빈다면 / DFS밖 모든 for문이 끝난다면, 사이클이 존재한다고 판단할 수 있다.
#   이때는 visited를 사용하여 모든 원소가 방문되었는지 확인해야 하겠다.

# init
n, m = map(int, input().split())
adj = defaultdict(list)
indeg = [-1] + [0] * n
for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    adj[u].append(w)
    indeg[w] += 1
# end of init

# using DFS
def DFS(v, adj, indeg):
    print(v, end=' ')
    for w in adj[v]:
        indeg[w] -= 1           # 탐색.
        if indeg[w] == 0:       # 진입 차수가 0이 된 정점들을
            DFS(w, adj, indeg)  # 방문.

for v in [i for i,d in enumerate(indeg) if d ==0]:  # 그래프의 처음 상태에서, 각 연결요소 중 진입 차수가 0 인 정점은 하나씩 밖에 없다.
                                                    # 그래서 초기화 시에 indeg(진입차수)가 0인 정점들만 돌면서 DFS해주면 된다.
    DFS(v, adj, indeg)