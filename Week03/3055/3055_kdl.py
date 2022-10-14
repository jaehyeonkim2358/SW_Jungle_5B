import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

R, C = map(int, input().split())

ddiddup = [list(input().rstrip()) for _ in range(C)]

for i in range(C):
    for j in range(R):
        if ddiddup[i][j] == 'D':
            start = (i, j)
        if ddiddup[i][j] == 'S':
            end = (i, j)

print(ddiddup)

# def bfs():

# *에서 인접한 노드를 *로 한다. > 물이 미리 찰 것이니까 X는 돌이니까 적용 안됨
# 비버의 위치에서 인접한 노드 (.)에 1씩 더한다.
# 인접한 노드에 s가 있으면 break하고 해당 값을 리턴한다.
# 만약에 움직일 수 있는 곳이 없으면 kaktus를 리턴한다?ㄴ
