import sys
sys.stdin = open('Week04/9084/9084_lwh.txt', 'r')
input = sys.stdin.readline

T = int(input())
# 1, 5, 10, 50, 100, 500

def init():
    
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    a = [0] * 10001
    a[0] = 1

    # 동전을 통제하는 거다 !!!! 동전을 통제해!!! 동전을 통제해라!!!
    for coin in coins:
        for i in range(M+1):
            if i >= coin:    
                a[i] += a[i-coin]

    print(a[M])


for _ in range(T):
    init()