import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
A = [[] for _ in range(n)]
start = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        A[i].append(tmp[j])
        if tmp[j] > 0:
            start.append((i, j))


move = ((1, 0), (0, 1), (-1, 0), (0, -1))
def solution(start):
    global n, m
    queue = deque(start)
    count = [[0] * m for _ in range(n)]
    year = 0

    while queue:
        year += 1
        for cur in queue:
            count[cur[0]][cur[1]] = 0
            for mx, my in move:
                nextX = cur[0] + mx
                nextY = cur[1] + my
                if check(nextX, nextY):
                    if A[nextX][nextY] == 0:
                        count[cur[0]][cur[1]] += 1
            if count[cur[0]][cur[1]] >= A[cur[0]][cur[1]]:
                A[cur[0]][cur[1]] = -1
            else:
                A[cur[0]][cur[1]] -= count[cur[0]][cur[1]]

        visited = [[0] * m for _ in range(n)]
        flag = False
        size = len(queue)
        while size > 0:
            size -= 1
            r, c = queue.popleft()
            if A[r][c] == -1:
                A[r][c] = 0
            else:
                queue.append((r, c))
                if visited[r][c] == 0:
                    if flag:
                        return year
                    visited[r][c] = 1
                    flag = True
                    bfs((r, c), visited)
    return 0


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


def check(x, y):
    global n, m
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    return True


print(f'{solution(start)}')
