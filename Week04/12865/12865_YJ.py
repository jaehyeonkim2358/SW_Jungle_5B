import sys
sys.stdin = open("input.txt","r")

# 입력값 받기 
N,K = map(int, input().split())
items = [(0,0)] # (value, weight) 순 
for i in range(N) :
    w,v = map(int,input().split())
    items.append((w,v))

#dp 테이블은 (N+1)*(K+1)의 2차원 배열로 생성
dp = [[None for _ in range(K+1)] for __ in range(N+1)]

# top-down으로 내려가는 knapsack 함수 생성 
def knapsack(n,w) :
    if n==0 or w== 0:
        return 0 
    if dp[n][w] == None: 
        if w-items[n][0] >= 0 : # 가방에 무게가 남았다면
            dp[n][w] = max(knapsack(n-1, w-items[n][0])+items[n][1],knapsack(n-1,w))
        else: # 가방에 무게가 부족하다면
            dp[n][w] = knapsack(n-1, w)
    return dp[n][w]

print(knapsack(N,K))