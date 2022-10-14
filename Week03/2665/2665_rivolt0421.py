from collections import deque
import sys
sys.stdin = open("W03-W04/Week03/2665/input.txt","r")

# initializing
n = int(input())
maze=[]
for _ in range(n):
    maze.append(sys.stdin.readline().strip())
visited = set([(0,0)])
q=deque([[0,0, 0]])
#        [r,c, b(검->흰 바꾼 횟수)]
# end of initializing

def wall_check(r,c):
    if r < 0 or n <= r:     # 위아래 범위 밖
        return -1
    if c < 0 or n <= c:     # 양쪽 범위 밖
        return -1
    if maze[r][c] == '0':
        return 0            # 중간 벽
    return 1

# solution (BFS)
while q:
    point = q.popleft()
    if tuple(point[:2]) == (n-1,n-1) :     # 도착한 경우
        print(point[2])
        
    for r,c in [(-1,0),(1,0),(0,-1),(0,1)]: # 상,하,좌,우
        next = [point[0]+r , point[1]+c, point[2]]
        if tuple(next[:2]) not in visited:
            check = wall_check(*next[:2])
            
            if check == -1:       # 미로 범위 밖
                continue
            
            elif check == 1:      # 흰 방
                q.appendleft(next)                         # 흰 방의 경우 appendleft를 해줘서 탐색 우선순위의 우위를 주고,
                visited.add(tuple(next[:2]))
                
            else: # check == 0    # 검은 방                # 검은 방의 경우 append를 해줘 탐색 우선수위에서 밀리게 한다.
                q.append([next[0],next[1], next[2]+1])              
                visited.add(tuple(next[:2]))
                                                           # 이는 우선수위 큐로도 구현 가능하다.
                                                           
# visited 배열 사용 버전

# # initializing
# n = int(input())
# maze=[]
# for _ in range(n):
#     maze.append(sys.stdin.readline().strip())
# visited = [[-1]*n for _ in range(n)]
# visited[0][0] = 0
# q=deque([(0,0)])
# # end of initializing

# def wall_check(r,c):
#     if r < 0 or n <= r:     # 위아래 범위 밖
#         return -1
#     if c < 0 or n <= c:     # 양쪽 범위 밖
#         return -1
#     if maze[r][c] == '0':
#         return 0            # 중간 벽
#     return 1

# # solution (BFS)
# while q:
#     point = q.popleft()
#     if point == (n-1,n-1) :     # 도착한 경우
#         print(visited[point[0]][point[1]])
        
#     for r,c in [(-1,0),(1,0),(0,-1),(0,1)]: # 상,하,좌,우
#         next = (point[0]+r , point[1]+c)
#         check = wall_check(*next)
#         if check >= 0 and visited[next[0]][next[1]] == -1:
#             if check == 1:      # 흰 방
#                 q.appendleft(next)  
#                 visited[next[0]][next[1]] = visited[point[0]][point[1]]
#             else: # check == 0    # 검은 방
#                 q.append(next)
#                 visited[next[0]][next[1]] = visited[point[0]][point[1]] + 1