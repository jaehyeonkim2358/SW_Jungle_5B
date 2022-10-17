import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")


############### bfs를 이용한 풀이 ############### 37972kb 1456ms
# from collections import deque

# n, m = map(int, sys.stdin.readline().strip().split())
# visited = [[] for _ in range(n + 1)]
# danger_rock = set()
# for _ in range(m) :
#     danger = int(input())
#     danger_rock.add(danger)

# def bfs(n, visited, danger_rock) :
#     q = deque([(1, 0, 0)])
#     while q :
#         cur, jump, cnt = q.popleft()
#         for x in [jump - 1, jump, jump + 1] :
#             if x > 0 :
#                 next = cur + x
#                 if next == n :
#                     return cnt + 1
#                 if next < n and next not in danger_rock and x not in visited[next] :
#                     visited[next].append(x)
#                     q.append((next, x, cnt + 1))
#     return -1

# print(bfs(n, visited, danger_rock))
############################################################


############### DP를 이용한 풀이 ############### 44264KB 724ms
n, m = map(int, sys.stdin.readline().strip().split())
INF = float('inf')
dp = [[INF] * (int((2*n)** 0.5) + 2) for _ in range(n+1)]
dp[1][0] = 0    # dp[i][j] = 현재 위치 i에서 j의 속도

danger_rock = set()
for _ in range(m) :
    danger_rock.add(int(sys.stdin.readline().strip()))
# print(danger_rock)

# 풀이
for i in range(2, n + 1) :
    if i in danger_rock :
        continue
    for j in range(1, int((2*i)**0.5) + 1) :
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

if min(dp[n]) == INF :
    print(-1)
else :
    print(min(dp[n]))