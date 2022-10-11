import sys
from heapq import heappush, heappop
sys.stdin = open('2665/2665_lwh.txt', 'r')
input = sys.stdin.readline

# 검은 방 : 0
# 흰 방 : 1
# dijkstra : 바꾼 방 수 = room, heapq 써서 room 가장 적은 지점들에서 부터 나아가며 탐색 
# heap 에 (room, (x, y))로 넣기

def dijkstra(maze, n):

    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    q = []
    heappush(q, (0, (0, 0)))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        room, u = heappop(q)

        if u[0] == n-1 and u[1] == n-1:
            print(room)

        for i in range(4):
            vx, vy = u[0] + dx[i], u[1] + dy[i]
            if vx <= -1 or vx >= n or vy <= -1 or vy >= n:
                continue
            if not visited[vx][vy]:
                visited[vx][vy] = True

                if maze[vx][vy] == '0':
                    heappush(q, (room+1, (vx, vy)))
                else:
                    heappush(q, (room, (vx, vy)))



def init():

    n = int(input())
    maze = [list(input().rstrip()) for _ in range(n)]
    
    dijkstra(maze, n)


init()