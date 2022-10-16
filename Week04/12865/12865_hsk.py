import sys
sys.stdin = open("input.txt","r")
# 05. https://www.acmicpc.net/problem/12865: 평범한 배낭
input = sys.stdin.readline

# 1차원--------------------------
# https://myjamong.tistory.com/319
# 물건의 수, 담을 수 있는 수 
# n = 4, k = 7
n, k = map(int, input().split())
# 물건의 무게, 가치
# w_v = [(6, 13), (4, 8), (3, 6), (5, 12)]

dp = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())

    for i in range(k, w-1, -1):
        dp[i] = max(v + dp[i-w], dp[i]) 
print(max(dp))








# 2차원--------------------------
# 물건의 수, 담을 수 있는 수 
# n = 4, k = 7
# n, k = map(int, input().split())
# # 물건의 무게, 가치
# # w_v = [(6, 13), (4, 8), (3, 6), (5, 12)]
# w_v = [[0,0]]
# for i in range(n):
#     w, v = map(int, input().split())
#     w_v.append((w,v))

# dp = [[0] * (k+1) for _ in range(n+1)]

# for i in range(1,n+1): # 행 i (물건 무게)
#     weight = w_v[i][0]
#     value = w_v[i][1]
#     for j in range(1, k+1): # 열 j (담을 수 있는 무게)
#         if j < weight:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-weight]+ value, dp[i-1][j])

# print(dp[n][k])





