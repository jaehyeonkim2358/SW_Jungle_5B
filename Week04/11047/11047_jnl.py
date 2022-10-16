# 동전 0
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split(' '))
coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

def solution():
    global K
    cnt = 0
    while K > 0 and coins:
        coin = coins.pop()
        if K >= coin:
            cnt += K // coin
            K  -= (K // coin) * coin
    return cnt

print(f'{solution()}')