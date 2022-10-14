import sys
from collections import defaultdict
from heapq import heappop, heappush

# 1.
# 정답이 여러개일 경우
# 사전순으로 가장 앞서는 것을 출력해주어야 한다.

# 2.
# 일반적인 위상 정렬은, 
# 진입 차수가 0인 정점들로부터 시작하여
# 연결된 정점의 진입 차수를 감소시키며(간선을 지우며)
# 이들의 진입 차수가 0이 되면, 
# 해당 정점에 연결된 다른 정점을 찾는 방법으로
# DAG(Directed Acyclic Graph; 방향 비순환 그래프)의 정점을 정렬한다.

# 3.
# 즉, 앞선 정점들(첫 입력 부터 진입 차수가 0이었던 정점들)을 먼저 정렬하고,
# 뒤 이은 정점들(이후 위상 정렬을 진행하며 진입 차수가 0이 된 정점들)을 이후에 정렬하는 방식이다.
# 이는 다른 말로, 
# 정렬의 우선순위가 
# 진입 차수가 0인 정점으로부터 먼 정점 순(진입 차수의 크기와 비례하지 않음)으로 주어진다는 의미이다.

# 4.
# 문제의 조건을 다시 보면
# 그래프의 각 정점를 위상 정렬할 때,
# 그 순서가 여러가지(모든 정점이 각각 하나의 순서만을 갖지 않는 경우)라면
# 그 중 오름차순으로 가장 앞선 순서를 출력해주어야 한다.

# 5.
# 문제가 원하는 형태로 정렬된 순서를 출력하기 위해서는
# 실제 정렬 순서를
# '우선순위가 낮은것부터, 우선순위가 높은것 순으로' 정렬해주어야 한다.
# 그러니까, 우선순위 A, B에 대해서,
# 'A를 기준으로 정렬하고 A가 같은 것들은 B를 비교해서 정렬해주세요' 라고 했을 때
# 'B'로 먼저 정렬한 뒤, 'A'로 정렬해주어야 
# 요구하는 우선순위대로 정렬된다는 이야기다.

# 6.
# 따라서, 진입 차수가 0인 정점의 우선순위를 가장 낮게하여 위상 정렬을 해 주어야 하고
# 이를 위해서는 그래프 방향을 반대로(진출 방향) 탐색해 주어야 한다.

# 7.
# 입력되는 그래프의 간선 방향을 반대로 받아준 뒤
# 진입 차수가 아닌 진출 차수를 이용하고
# Max Heap을 이용해 각 정점 번호가 큰 순서로 큰 숫자를 등수로 갖도록 구현했다.
# 같은 형태의 그래프를 반대로 위상정렬 하고,
# 그 과정에서 등수 계산을 반대로 해 준 것이다.
# 또한, 순환 여부를 판단하기 위해
# 첫 입력부터 진출 차수가 0인 정점이 없거나,
# 위상 정렬 도중 같은 정점의 등수를 2번 이상 갱신하려고 시도할 때
# 순환이 존재하여 순서를 구할 수 없는 그래프라고 판단했다.

n = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
out_degree = [0] * (n+1)

for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip()
    for j in range(n):
        if tmp[j] == '1':
            graph[j+1].append(i)
            out_degree[i] += 1


rank = [0] * (n+1)
def bfs(n):
    q = []
    for i in range(1, n+1):
        if out_degree[i] == 0:
            heappush(q, -i)
    if q == []:
        return False

    count = n
    while q:
        cur = -heappop(q)
        rank[cur] = count
        count -= 1
        for next in graph[cur]:
            out_degree[next] -= 1
            if out_degree[next] == 0:
                if rank[next] != 0:
                    return False
                heappush(q, -next)
    return True


if bfs(n):
    for r in rank[1:]:
        sys.stdout.write(f'{r} ')
else:
    sys.stdout.write('-1')
