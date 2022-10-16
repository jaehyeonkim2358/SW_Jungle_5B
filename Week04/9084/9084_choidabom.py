# 9084: 동전
# 1원, 5원, 10원, 50원, 100원, 500원
# 예를 들어, 30원을 만들기 위해 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법 가능
# 동전의 종류가 주어질 때 주어진 금액을 만드는 모든 방법 세라 !

import sys
sys.stdin = open("9084/input.txt","r")
input = sys.stdin.readline
   
ans = []
coin = []
T = int(input().rstrip()) # 테스트 케이스 개수 T
for i in range(T):
    N = int(input().rstrip()) # 동전의 가지수 N
    coins = list(map(int, input().split()))
    M = int(input()) # 주어진 N가지 동전으로 만들어야할 금액 M
    
    # memoizations을 위한 리스트 선언
    dp = [0 for _ in range(M+1)] 
    dp[0] = 1

    for coin in coins: # coin의 관점에서 먼저 봐야해. coin =[2, 3, 5]
        for i in range(M+1):
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])