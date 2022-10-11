import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
maze = [list(map(int, str(input().rstrip())))for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(n, m):
    # 큐를 만들어준다.
    queue = deque()
    # 시작점을 큐에 넣어준다.
    queue.append([n, m])
    while queue:
        n, m = queue.popleft()
        for cursor in direction:
            next_n = n + cursor[0]
            next_m = m + cursor[1]
            # 모든 방향을 돌면서 안가본 길(1)을 탐색한다.
            if 0 <= next_n < N and 0 <= next_m < M:
                if maze[next_n][next_m] == 0:
                    continue
                # 만약에 이동이 불가능하면 멈춘다.
                if maze[next_n][next_m] == 1:
                    # 주변의 탐색점에 1이 있으면 거기로 간다. 왜? 길이니까
                    maze[next_n][next_m] = maze[n][m] + 1
                    # 도착한 지점의 숫자를 +1한다
                    queue.append([next_n, next_m])
                    # 마지막 도착지의 숫자를 print한다.
    print(maze[N-1][M-1])


bfs(0, 0)
