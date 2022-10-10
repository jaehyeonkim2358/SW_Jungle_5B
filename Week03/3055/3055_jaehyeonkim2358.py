import sys
from collections import deque


def solution(start, end, water):
    h_queue = deque([start])        # 고슴도치의 좌표를 담을 덱
    w_queue = deque(water)          # 물의 좌표를 담을 덱
    count = 0                       # 발생 시간

    while h_queue:
        # 물의 이동이 예정된 곳으로는 이동하지 못하므로,
        # 물을 먼저 이동시킨다.
        w_size = len(w_queue)
        while w_size > 0:
            w_size -= 1
            w_cur = w_queue.popleft()
            for mv in move:
                w_nextX = w_cur[0] + mv[0]
                w_nextY = w_cur[1] + mv[1]
                if move_check(w_nextX, w_nextY, is_water=True):
                    w_queue.append((w_nextX, w_nextY))
                    forest[w_nextX][w_nextY] = '*'
        
        # 고슴도치 이동
        h_size = len(h_queue)
        while h_size > 0:
            h_size -= 1
            h_cur = h_queue.popleft()
            if h_cur[0] == end[0] and h_cur[1] == end[1]:
                return count
            for mv in move:
                h_nextX = h_cur[0] + mv[0]
                h_nextY = h_cur[1] + mv[1]
                if move_check(h_nextX, h_nextY, is_water=False):
                    h_queue.append((h_nextX, h_nextY))
                    # 방문 여부를 임의의 문자열 &로 체크해주었음
                    forest[h_nextX][h_nextY] = '&'
        count += 1
    return "KAKTUS"


# 이동 가능한 위치인지 확인해주는 함수
def move_check(x, y, is_water):
    global R, C
    
    # 배열 범위 바깥
    if x < 0 or x >= R:
        return False
    elif y < 0 or y >= C:
        return False

    # 물과 고슴도치 모두 이동할 수 없는 곳(돌, 물)
    elif forest[x][y] == 'X' or forest[x][y] == '*':
        return False
        
    # 물이 이동할 수 없는 곳(비버네 집)
    elif is_water and forest[x][y] == 'D':
        return False

    # 고슴도치가 이동할 수 없는 곳(이전 방문 위치)
    elif not is_water and forest[x][y] == '&':
        return False
    else:
        return True


R, C = map(int, sys.stdin.readline().split())
forest = [[] for _ in range(R)]
water = []
move = ((1, 0), (0, 1), (-1, 0), (0, -1))
for i in range(R):
    tmp = sys.stdin.readline().rstrip()
    for j in range(C):
        forest[i].append(tmp[j])
        if tmp[j] == '.':
            continue
        if tmp[j] == '*':
            water.append((i, j))
        elif tmp[j] == 'D':
            end = (i, j)
        elif tmp[j] == 'S':
            start = (i, j)
        

ans = solution(start, end, water)
sys.stdout.write(f'{ans}')
