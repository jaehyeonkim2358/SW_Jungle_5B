import sys
from collections import deque


def solution(queue):
    global raw_tomato
    queue = deque(queue)
    date = 0
    while queue:
        cur = queue.popleft()
        for mv in move:
            nextZ = cur[1] + mv[0]
            nextX = cur[2] + mv[1]
            nextY = cur[3] + mv[2]

            # 1. 토마토 상자의 범위를 벗어나거나, 
            # 2. 토마토가 없는 칸 이거나, 
            # 3, 이미 익은 토마토가 있는 칸 일 경우 
            # 진행하지 않음
            if check_tomato(nextZ, nextX, nextY) is False:
                continue

            if tomato_box[nextZ][nextX][nextY] == 0:
                raw_tomato -= 1                                 # 익지않은 토마토 개수 1 감소
                date = cur[0]+1                                 # 마지막으로 갱신된 날짜 = 모든 토마토가 익을때 까지 걸린 날
                tomato_box[nextZ][nextX][nextY] = 1             # 토마토 익히기
                queue.append((cur[0]+1, nextZ, nextX, nextY))   # 익은 토마토는 다른 토마토를 익힐 수 있으므로, append()
    return date


def check_tomato(z, r, c):
    global h, m, n
    if z < 0 or z >= h:
        return False
    if r < 0 or r >= n:
        return False
    if c < 0 or c >= m:
        return False
    if tomato_box[z][r][c] < 0 or tomato_box[z][r][c] > 0:
        return False
    return True
    

move = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

m, n, h = map(int, sys.stdin.readline().split())
tomato_box = [[[0] * (m) for _ in range(n)] for __ in range(h)]
start = []
raw_tomato = 0
for i in range(h):
    for j in range(n):
        tmp = sys.stdin.readline().split()
        for k in range(m):
            if int(tmp[k]) == 1:
                start.append((0, i, j, k))
            elif int(tmp[k]) == 0:
                raw_tomato += 1
            tomato_box[i][j][k] = int(tmp[k])


answer = solution(start)
if raw_tomato > 0:
    sys.stdout.write('-1')
else:
    sys.stdout.write(f'{answer}')