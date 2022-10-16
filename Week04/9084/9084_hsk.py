import sys
sys.stdin = open("input.txt","r")
# 03. https://www.acmicpc.net/problem/9084: 동전
input = sys.stdin.readline
# 1, 5, 10, 100, 500
# 케이스
t = int(input())

for i in range(t):
    # 동전의 가지수 1~20
    n = int(input())

    # n 가지 동전의 각각 금액(오름차순)
    coin_list = list(map(int, input().split()))
    # 금액
    money = int(input())
    # 동전별 확률을 찍을 dp
    dp = [0] * (money+1)
    dp[0] = 1
    for coin in coin_list:
        for x in range(1, money+1):
            # 동전이 오름차순이기 때문에 동전 숫자보다 작은 수는 볼필요가 없나? 
            # 근데 왜 index에러가 해결?
            if x >= coin:                 
                dp[x] = dp[x] + dp[x-coin]
    result = dp[-1]
    print(result)
        
            
 

