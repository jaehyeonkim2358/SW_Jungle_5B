import sys, heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, list(input().rstrip()))))


complete = [[0] * n for _ in range(n)]

heap = []

count_1 = 0

def bfs(count, x, y):
    heapq.heappush(heap, (count, x, y))
    if complete[x][y] == 0:
        complete[x][y] = 2
    else:
        complete[x][y] =1
    con_x = [-1, 1, 0, 0]
    con_y = [0, 0, -1, 1]

    while heap:
        count1, old_x, old_y = heapq.heappop(heap)

        if old_x == n-1 and old_y == n-1:
            return count1

        for i in range(4):
            new_x = old_x + con_x[i]
            new_y = old_y + con_y[i]

            if n > new_x >= 0 and n > new_y >= 0 and complete[new_x][new_y] == 0:

                if arr[new_x][new_y] == 1:
                    complete[new_x][new_y] = complete[old_x][old_y]
                    heapq.heappush(heap, (count1+1, new_x, new_y))
                else:
                    heapq.heappush(heap, (count1-1, new_x, new_y))

                if complete[new_x][new_y] == 0:
                    complete[new_x][new_y] = 2
                else:
                    complete[new_x][new_y] = 1




print(bfs(count_1, 0,0))
print(complete)