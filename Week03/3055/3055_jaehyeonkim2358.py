import sys
from collections import deque


def solution(start, end, water):
    h_queue = deque([start])
    w_queue = deque(water)
    count = 0

    while h_queue:
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
                    forest[h_nextX][h_nextY] = '&'
        count += 1
    return "KAKTUS"


def move_check(x, y, is_water):
    global R, C
    if x < 0 or x >= R:
        return False
    elif y < 0 or y >= C:
        return False
    elif forest[x][y] == 'X' or forest[x][y] == '*':
        return False
    elif is_water and forest[x][y] == 'D':
        return False
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
        

# 빈곳: '.'
# 물: '*'
# 돌: 'X'
ans = solution(start, end, water)
sys.stdout.write(f'{ans}')
