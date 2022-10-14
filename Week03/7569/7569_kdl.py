import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatomato = [[list(map(int, input().split()))
               for _ in range(N)] for _ in range(H)]


m_move = (1, -1, 0, 0, 0, 0,)
n_move = (0, 0, 1, -1, 0, 0,)
h_move = (0, 0, 0, 0, 1, -1)


def get_tomatomato():
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatomato[h][n][m] == 1:
                    queue.append((h, n, m))

    while queue:

        # 일단 bfs 탐색을 진행하자
        h, n, m = queue.popleft()
        for i in range(6):  # 6개의 방향을 탐색하여야 하므로.. (상,하,좌,우,전,후)
            new_h = h + h_move[i]
            new_n = n + n_move[i]
            new_m = m + m_move[i]

            if 0 <= new_h < H and 0 <= new_n < N and 0 <= new_m < M:
                if tomatomato[new_h][new_n][new_m] == 0:
                    tomatomato[new_h][new_n][new_m] = tomatomato[h][n][m] + 1
                    queue.append((new_h, new_n, new_m))


get_tomatomato()

tomatomato_ = True
res = -2
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatomato[h][n][m] == 0:
                tomatomato_ = False
                break
            else:
                res = max(tomatomato[h][n][m], res)

if tomatomato_:
    print(res-1)
if tomatomato_ == False:
    print(-1)
