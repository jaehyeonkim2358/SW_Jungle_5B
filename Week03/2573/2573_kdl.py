import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def melt(y, x):  # 얼음을 얼마나 녹일지 구현하는 함수 melt
    # x, y를 반대로 받는 이유는 좌료가 배열에서는 x,y좌표의 반대로 이뤄지기 때문
    h = 0  # 녹일 얼음의 높이 초기화.

    for i in direction:  # 상하좌우 모든 배열을 확인
        ny = y + i[1]
        nx = x + i[0]

        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] == 0:  # 주변에 바다가 있으면
                h += 1  # 녹일 얼음의 크기는 1 높아짐.

    return y, x, h


def dfs(y, x):  # 연결되어 있는 빙산이 있는지 찾아보자.
    if visited[y][x] == 'no':  # 연결된 얼음이 있다면 방문처리
        visited[y][x] = 'yes'

        for i in direction:
            ny = y + i[1]
            nx = x + i[0]

            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] != 0 and visited[ny][nx] == 'no':  # 물이 아니라면!
                    dfs(ny, nx)  # 그 주변도 싹 돌면서 방문 처리


N, M = map(int, input().split())  # 2차원 배열의 행과 열 입력
matrix = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력
year = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상,하,좌,우 확인하기 위해 방향 구현


while 1:
    year += 1
    melt_list = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:  # 모든 배열을 순회하면서 얼음을 발견
                row, col, height = melt(i, j)  # 해당 배열을 melt함수를 통해 녹일 높이를 구함.
                if height != 0:
                    # 녹일 높이가 있다면, 해당 정보를 melt list에 저장
                    melt_list.append([row, col, height])
    for row, col, height in melt_list:  # melt list에 저장된 모든 얼음들을 녹임
        # 음수일 경우 0이 나오도록 함.
        matrix[row][col] = max(matrix[row][col] - height, 0)

    cnt = 0
    visited = [['no'] * M for _ in range(N)]  # 방문 현황 초기화
    # 얼음 녹이고 난 뒤 빙하 개수 새기
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 'no' and matrix[i][j] != 0:
                dfs(i, j)
                cnt += 1
                # 빙하를 순회하면서 상하좌우를 확인하고 방문한 지역도 아니고, 얼음이라면, +1
                if cnt == 2:  # 빙산이 분리되는 순간 방신 탐색 종료
                    break
    if cnt > 1:
        break
    if sum(map(sum, matrix[1:-1])) == 0:  # 빙산이 모두 녹았는데 얼음이 1개면
        year = 0
        break

print(year)
