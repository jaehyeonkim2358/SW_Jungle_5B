import sys
from collections import deque

def is_bipartite_graph(start):
    global V
    # 방문안함 = 0, 정점집합1 = 1, 정점집합2 = -1
    
    flag = 1
    visited[start] = flag
    queue = deque([start])

    while queue:
        size = len(queue)
        flag *= -1
        for _ in range(size):
            cur = queue.popleft()
            for next in edges[cur]:
                if visited[next] == 0:
                    visited[next] = flag
                    queue.append(next)
                elif visited[next] != flag:
                    return False
    return True

testcase = int(sys.stdin.readline().rstrip())

for _ in range(testcase):
    V, E = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        v, u = map(int, sys.stdin.readline().split())
        edges[v].append(u)
        edges[u].append(v)

    visited = [0] * (V+1)
    # 그래프가 끊어져있는(모든 정점이 서로 연결되어있지는 않은)경우가 존재 할 수 있으므로
    # 방문하지 않은 모든 정점을 시작점으로 하여 이분 그래프 여부를 확인해줌
    for i in range(1, V+1):
        if visited[i] == 0:
            if is_bipartite_graph(i) is False:
                sys.stdout.write('NO\n')
                break
    else:
        sys.stdout.write('YES\n')
        
