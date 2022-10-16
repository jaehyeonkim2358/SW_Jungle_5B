import sys
sys.stdin = open("12865/input.txt","r")
input = sys.stdin.readline

# N: 물품의 수, K: 준서가 버틸 수 있는 무게
N, K = map(int, input().split())
stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))
# stuff = [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]
# => [weight, value]

# 물건들의 가치를 일단 모두 0으로 초기화
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


# 물품을 통제해라 !!!
for i in range(1, N+1): # 물품이 1부터 N개까지 탐색
    for j in range(1, K+1): # 무게 1부터 무게 K까지 탐색
        w = stuff[i][0] # 무게
        v = stuff[i][1] # 가치

        if j < w:
            dp[i][j] = dp[i-1][j]
        else: 
            # 새로운거 안 넣고 그대로 가기 vs 새로운 물품의 무게만큼 비워서 새로운 물품 넣음 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])