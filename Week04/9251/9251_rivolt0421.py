import sys
sys.stdin = open("W03-W04/Week04/9251/input.txt","r")

S, T = sys.stdin.read().split()
r = len(S) ; c = len(T)
dp = [[0]*(c+1) for _ in range(r+1)]


# 1. LCS

for i in range(1,r+1):
    for j in range(1,c+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
print(dp[r][c])

# 2. 리벤슈타인 편집거리, 백트레이싱으로 '비용 안드는 대체연산' 횟수 계산.
    # 배열 초기화
# for i in range(c+1):
#     dp[0][i] = i
# for j in range(r+1):
#     dp[j][0] = j

# # 2-1. 비용 없이 대체연산 가능하다면, 다른 방향의 값들과의 비교 없이 무조건 대체연산한다.    
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         if S[i-1] == T[j-1]:
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
            
# # 2-2. 대체연산의 비용 유무와 관계 없이, 무조건 방향들 간의 최소값을 고른다.
# # 이 방법으로 계산하고 이후에 back-tracing으로 LCS의 길이를 찾으려고 하면 틀린 값이 나온다.
# # for i in range(1,r+1):
# #     for j in range(1,c+1):
# #         dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (0 if S[i-1] == T[j-1] else 1))
        
# untact = 0
# while r > 0 and c > 0:  # back-tracing
#     if S[r-1] == T[c-1]:
#         untact += 1
#         r, c = r-1, c-1
#         continue
    
#     r, c = min((dp[r-1][c] + 1, (r-1, c)),
#              (dp[r][c-1] + 1, (r, c-1)))[1]
    
# print(untact)