import sys
from heapq import heappop, heappush


# 다엘이들을 시켜서 미로를 만들자.
# 각 다엘이들은 현재 위치(x, y)와 검은방을 흰방으로 바꿔준 횟수(count)를 지니고 있다.
class KDL:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count

    def __lt__(self, other):
        return self.count < other.count


def solution(start):
    global INF, n
    queue = [start]

    # visited: 최단경로 추정값. 각 지점에 방문하기 위해 바꿔준 방의 수를 최소값으로 갱신하는 이중 리스트
    visited = [[INF] * (n) for _ in range(n)]
    visited[start.x][start.y] = 0

    while queue:
        # 현재 다엘이를 꺼냄
        # 이때, '방을 바꿔준 횟수가 작은 다엘이' 부터 꺼내주기 위해 count를 오름차순으로 정렬하는 min-heap을 사용
        cur = heappop(queue)

        # 현재 다엘 지점에서 인접한 4가지 이동 경로를 모두 확인
        for m in move:
            nextX = cur.x + m[0]
            nextY = cur.y + m[1]

            # 다엘이가 이동할 수 없는 곳(배열 범위 바깥)일 경우 진행하지 않음
            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n:
                continue

            # 다엘이가 이동하려는 곳이 하얀 방 일 때
            if room[nextX][nextY] == '1':
                # '현재 다엘이가 바꿔준 방의 수'가 visited에 저장된 '바꿔준 방 수의 최소값' 보다 더 적을 때만 진행
                if visited[nextX][nextY] > cur.count:
                    heappush(queue, KDL(nextX, nextY, cur.count))
                    visited[nextX][nextY] = cur.count
            # 다엘이가 이동하려는 곳이 검은 방 일 때
            else:
                # 검은 방으로 이동하기 위해서는 방을 한번 더 바꿔주어야 하기 때문에,
                # '현재 다엘이가 바꿔준 방의 수 + 1'이 visited에 저장된 '바꿔준 방 수의 최소값' 보다 더 적을 때만 진행
                if visited[nextX][nextY] > cur.count + 1:
                    heappush(queue, KDL(nextX, nextY, cur.count + 1))
                    visited[nextX][nextY] = cur.count + 1

    sys.stdout.write(f'{visited[n-1][n-1]}')


n = int(sys.stdin.readline().rstrip())

room = []
for _ in range(n):
    room.append(sys.stdin.readline().rstrip())

INF = 2**31
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
solution(KDL(0, 0, 0))