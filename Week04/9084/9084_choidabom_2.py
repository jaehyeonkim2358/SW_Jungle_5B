# 9084: 동전 
# 핵심은 동전을 통제하는거다.
import sys
sys.stdin = open("9084/input.txt","r")
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수 T

def init():
    N = int(input()) # 동전의 가지수 N
    coins = list(map(int, input().split()))
    M = int(input())  # 주어진 N가지 동전으로 만들어야할 금액 M

    # memoizations을 위한 리스트 선언
    dp = [0] * 23
    dp[0] = 1 # dp[0]을 1로 초기화하는 이유는??? 

    # 동전의 종류를 하나씩 풀어주면서, 
    # dp 테이블에 적어둔 조합 수를 갱신해나가면 된다. 
    # 구하고자 하는 것 자체가 N가지 동전으로 금액 M을 만드는 모든 방법의 수이기 때문! 
    # 적은 금액부터 동전을 다 내어주면서 (coins for문이 안쪽으로 들어가면) 가지 수를 갱신하면 중복의 경우가 생긴다. 
    for coin in coins:
        for i in range(M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])

for i in range(T):
    init()