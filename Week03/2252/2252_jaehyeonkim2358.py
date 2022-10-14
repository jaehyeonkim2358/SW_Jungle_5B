from sys import stdin, stdout
from collections import deque
input = stdin.readline
print = stdout.write


def solution():
    global n
    queue = deque()

    # 진입 차수가 0인 학생을 queue에 저장하고 방문 처리
    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)
    
    # 진입 차수가 0인 학생을 한명씩 꺼내며 순회
    while queue:
        cur = queue.popleft()
        print(f'{cur} ')
        # 현재 순회중인 학생과 연결된 학생들을 순회
        for next in edges[cur]:
            # 꺼낸 학생과 연결된 학생의 진입 차수를 감소시킴(간선을 지움)
            in_degree[next] -= 1
            # 진입 차수가 0이면 queue에 저장
            if in_degree[next] == 0:
                queue.append(next)


# 입력
n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)             # 정점을 index로 하는, 정점의 진입 차수를 저장할 리스트
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    in_degree[b] += 1

solution()