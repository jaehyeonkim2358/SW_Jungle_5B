import sys
from collections import deque
sys.stdin = open('3055/3055_lwh.txt', 'r')
input= sys.stdin.readline

# 비버 굴 D
# 고슴도치 위치 S
# 물 * 돌 X
# 물, 고슴도치는 돌 통과 X
# 고슴도치 물 통과 X, 물 인접 통과 X
# 물 비버굴 통과 X

# 굴까지 가는 경로에 고슴도치가 물보다 늦게 혹은 동시에 도착하는 지점이 있으면 안됨 
# 물 도착시간 먼저 매핑 후 고슴도치가 물을 피해서 굴까지 가는 최단 경로 찾기
# v.time > u.time + 1 일때 v로 이동
# 굴은 물갈땐 0 으로 막아두고 INF 초기화 . 고슴도치 스캔 후 결과 출력 그대로 INF이면 안간 것


def run(forest, s, R, C):
    q = deque()
    q.append(s)

    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    while q:
        u = q.popleft()
        ux, uy = u[0], u[1]
        utime = forest[ux][uy]
    
        for i in range(4):
            vx, vy = ux + dx[i], uy + dy[i]
            if vx <= -1 or vx >= R or vy <= -1 or vy >= C:
                continue

            if forest[vx][vy] > utime + 1:
                forest[vx][vy] = utime + 1
                v = (vx, vy)
                q.append(v)


def init():
    
    R, C = map(int, input().split())
    forest = [[False]*C for _ in range(R)]
    
    INF = 2**31

    water = []
    for x in range(R):
        row = list(input().rstrip())
        for y in range(C):
            obj = row[y]
            forest[x][y] = obj
            if obj == 'D':
                forest[x][y] = 0
                cave = (x, y)
            elif obj == 'X':
                forest[x][y] = 0
            elif obj == 'S':
                forest[x][y] = INF
                kak = (x,y)
            elif obj == '*':
                forest[x][y] = 0
                water.append((x, y))
            else:
                forest[x][y] = INF
    
    if water:
        for s in water:
            run(forest, s, R, C)

    forest[cave[0]][cave[1]] = INF
    forest[kak[0]][kak[1]] = 0

    run(forest, kak, R, C)

    res = forest[cave[0]][cave[1]]

    if res == INF:
        print('KAKTUS')
    else:
        print(res)


init()
