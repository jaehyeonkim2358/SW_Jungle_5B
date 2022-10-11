import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 입력값 받기.
n_room = int(input())
matrix = []
for _ in range(n_room):
    matrix.append(list(map(int, input().rstrip())))
# 2차원 배열 구현
visited = [[False]*n_room for _ in range(n_room)]  # 방문여부 및 거리 체크
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 출발지를 입력하면 출발지에서 출발.
# bfs(start)
def bfs(break_num, col, row):
    # 큐를 만들어서 진행.
    p_queue = []
    # 우선순위 큐를 사용한 이유는 벽을 가장 적게 부순 경우를 확인하여야 하기 때문.
    # 벽을 부순 숫자로 정렬을 시키기 때문에 해당 경우만 선택해서 탐색이 가능함
    heappush(p_queue, (break_num, col, row))  # 들어간 검은색 방 숫자, 방의 위치
    # 기본적으로 검은색 방을 들어간다는 생각보다 벽을 부순다고 생각함.
    visited[col][row] = True
    while p_queue:
        break_num, col, row = heappop(p_queue)

        if col == n_room - 1 and row == n_room-1:
            print(break_num)
            break
            # 끝까지 도착했으면 그동안 부순 벽의 숫자를 print

        for d in direction:
            next_col = col + d[0]
            next_row = row + d[1]

            if 0 <= next_col < n_room and 0 <= next_row < n_room and visited[next_col][next_row] == False:
                # 범위를 벗어나지 않는 상태에서 방문한 적이 없다면
                if matrix[next_col][next_row] == 1:
                    # 하얀색 방 > 길이 있는 거임
                    heappush(p_queue, (break_num, next_col, next_row))
                if matrix[next_col][next_row] == 0:
                    # 길이 없고 방문을 안했으면 visited에 벽을 깬 cnt를 저장함.
                    heappush(p_queue, (break_num+1, next_col, next_row))
                visited[next_col][next_row] = True
                # 방문 여부 체크


bfs(0, 0, 0)
