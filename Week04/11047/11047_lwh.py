# 동전 문제
# 이분탐색으로 거슬러야 하는 돈보다 작은 애들중에 가장 큰 화폐를 찾은 후 
# 그리디하게 카운팅

import sys
sys.stdin = open('Week04/11047/11047_lwh.txt', 'r')
input = sys.stdin.readline 

# def bi_search():

#     s, e = 0, N - 1 
    
#     while True:
#         m = (s + e) // 2
#         coin = coins[m]
#         if coin == K:
#             return m
#         elif coin < K:
#             s = m + 1
#         else:
#             e = m - 1
        
#         if s > e:
#             break

#     return m
# N이 너무 작아서 이분탐색 하면 더 느림 

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0

for i in range(len(coins)-1, -1, -1):
    count += K // coins[i]
    K %= coins[i]

print(count)



