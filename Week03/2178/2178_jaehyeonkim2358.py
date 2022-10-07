import sys, heapq

n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())


move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def solution(start):
    global n, m
    queue = []
    visited = [[0] * m for _ in range(n)]
    queue.append(start)
    visited[start[0]][start[1]] = 1
    cnt = 0
    while queue:
        size = len(queue)
        cnt += 1
        while size > 0:
            cur = queue.pop(0)
            if cur[0] == n-1 and cur[1] == m-1:
                return cnt
            for mv in move:
                if check(cur[0]+mv[0], cur[1]+mv[1]):
                    if visited[cur[0]+mv[0]][cur[1]+mv[1]] == 0:
                        visited[cur[0]+mv[0]][cur[1]+mv[1]] = 1
                        queue.append([cur[0]+mv[0], cur[1]+mv[1]])
            size -= 1



def check(x, y):
    global n, m
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    if arr[x][y] == '0':
        return False
    return True


print(solution([0, 0]))