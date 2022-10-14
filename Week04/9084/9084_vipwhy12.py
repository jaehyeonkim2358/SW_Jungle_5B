#동전 

#방법도 생각 못했음 왜 생각 못했지

import sys

sys.stdin = open("백준/WEEK04/input.txt", "r")

#테스트 케이스의 개수
t = int(sys.stdin.readline())

for _ in range(t):
    # 동전의 가지 수 
    n = int(sys.stdin.readline())
    
    # n가지의 동전의 각 금액이 오름차순으로 제공
    coins = list(map(int, sys.stdin.readline().split()))
    #동전으로 만들어야 할 금액
    m = int(sys.stdin.readline())

    # 기억을 위한 리스트 선언
    dp = [0] * (m + 1)
    
    # 0원일때는 무조건 경우의 수가 1가지이다.
    dp[0] = 1
    
    for coin in coins:
        for i in range(1, m + 1):
            if i >= coin:
                dp[i] = dp[i - coin] + dp[i]
    
    print(dp[m])
    