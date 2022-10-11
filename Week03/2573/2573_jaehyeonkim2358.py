import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
A = [[] for _ in range(n)]
start = []      # 첫 빙산의 좌표를 튜플로 저장할 리스트
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        A[i].append(tmp[j])
        # 빙산의 좌표인 경우
        if tmp[j] > 0:
            start.append((i, j))


move = ((1, 0), (0, 1), (-1, 0), (0, -1))   # 어떤 좌표의 인접한 좌표(상,하,좌,우)를 확인하기 위한 리스트
def solution(start):
    global n, m
    queue = deque(start)                    # 빙산 위치를 담고있는 큐
    count = [[0] * m for _ in range(n)]     # 각 빙산에 인접한 바닷물 칸의 갯수를 저장할 2차원 리스트
    year = 0                                # 연도 계산을 위한 변수

    while queue:
        year += 1

        # 빙산에 인접한 바닷물 칸을 각각 게산해서, 녹을 예정인 빙산 높이를 count에 저장해주는 반복문
        for cur in queue:
            count[cur[0]][cur[1]] = 0
            for mx, my in move:
                nextX = cur[0] + mx
                nextY = cur[1] + my
                # 배열 범위 내의 좌표인지 확인하기
                if check(nextX, nextY):
                    # 인접한 바닷물 칸의 수 계산
                    if A[nextX][nextY] == 0:
                        count[cur[0]][cur[1]] += 1
            # 녹을 예정인 얼음을 -1로 갱신 : 0으로 갱신하면 다음 순회에서 이미 녹은 위치로 판단하기 때문
            if count[cur[0]][cur[1]] >= A[cur[0]][cur[1]]:
                A[cur[0]][cur[1]] = -1
            # 녹지 않은 빙산은 높이 감소
            else:
                A[cur[0]][cur[1]] -= count[cur[0]][cur[1]]


        visited = [[0] * m for _ in range(n)]   # 빙산 방문 체크
        flag = False                            # 최초 1회 탐색안에 모든 빙산을 방문할 수 있는지 여부를 체크
        size = len(queue)

        # 녹은 빙산과 그렇지 않은 빙산을 구분하여, 
        # 녹은 빙산은 빙산 좌표 큐에서 제거하고,
        # 녹지 않은 빙산을 이용해 전체 빙산의 연결 요소의 개수가 1보다 큰지 판단함
        while size > 0:
            size -= 1
            r, c = queue.popleft()
            # 녹은 빙산을 0으로 갱신
            if A[r][c] == -1:
                A[r][c] = 0
            # 녹지 않은 빙산의 경우
            else:
                queue.append((r, c))        # 다시 queue에 넣어줌.
                if visited[r][c] == 0:      # 방문하지 않은 좌표를 탐색.
                    if flag:                # 1회 탐색 이후에도 아직 방문되지 않은 빙산이 있을 경우
                        return year         # 빙산이 나눠진 것 이므로, 종료
                    visited[r][c] = 1
                    flag = True
                    bfs((r, c), visited)    # BFS 탐색으로 빙산 체크
    return 0


# BFS를 이용해서 연결 요소(빙산 덩어리)를  체크하는 함수
def bfs(s, visited):
    q = deque([s])
    while q:
        x, y = q.popleft()
        for mx, my in move:
            nx = x+mx
            ny = y+my
            if check(nx, ny) is False:
                continue
            if visited[nx][ny] == 0 and A[nx][ny] > 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


# 탐색하려는 좌표가 배열 범위 안에 존재하는지 확인하는 함수
def check(x, y):
    global n, m
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    return True


sys.stdout.write(f'{solution(start)}')
