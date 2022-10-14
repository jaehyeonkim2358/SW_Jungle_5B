import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 69912kb / 1560ms


def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:  # 색을 안칠했으면 색을 챌해준다.
            if visited[node] == 'red':  # 인접 노드의 색을 다르게 칠해준다.
                visited[i] = 'blue'
            elif visited[node] == 'blue':
                visited[i] = 'red'
            check = dfs(i)  # i의 인접노드도 확인한다.
            if not check:  # i의 인접노드도 확인했는데 색깔이 똑같다면 False를 return
                return False
        elif visited[node] == visited[i]:  # 인접노드와 색깔이 같다면
            return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visited = {i: 0 for i in range(1, V+1)}
    for _ in range(E):
        sv, ev = map(int, input().split())
        graph[sv].append(ev)
        graph[ev].append(sv)

    res = True
    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 'red'  # 방문 안했으면 일단 red로 칠한다.
            res = dfs(i)
            if not res:  # 색이 정상적으로 칠해졌으면 True이고 아니면 False
                break

    print('YES') if res is True else print('NO')
