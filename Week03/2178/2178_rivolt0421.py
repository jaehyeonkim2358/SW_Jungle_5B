from collections import deque
import sys
sys.stdin = open("W03-W04/Week03/2178/input.txt","r")

# initializing
n, m = map(int, input().split())
maze=[]
for _ in range(n):
    maze.append(sys.stdin.readline().strip())
visited = set([(0,0)])
q=deque([(0,0)])
# end of initializing

def wall_check(r,c):
    if r < 0 or n <= r:     # 위아래 끝
        return False
    if c < 0 or m <= c:     # 양쪽 끝
        return False
    if maze[r][c] == '0':
        return False        # 중간 벽
    return True

# solution (BFS)
steps = 0
while q:
    number_of_adjs = len(q)   # 이전 step에서 append 해준 만큼(각 경로의 wall_check 통과한 인접좌표의 수 총합만큼)
                            # pop을 해주는(a)게 핵심이다. 그래야 steps가 지켜진다.
    steps += 1
    
    while number_of_adjs > 0: # a
        point = q.popleft()   # a
        if point == (n-1,m-1) :     # 도착한 경우
            print(steps); exit();
        for r,c in [(-1,0),(1,0),(0,-1),(0,1)]: # 상,하,좌,우
            next = (point[0]+r , point[1]+c)
            if next not in visited and wall_check(*next):
                q.append(next)      # 여기서 append 되는 총 수와 number_of_adjs는 다르다.
                                    # number_of_adjs는 이전스텝에서 추가된 좌표들의 수이다.
                visited.add(next)
        number_of_adjs -= 1
    