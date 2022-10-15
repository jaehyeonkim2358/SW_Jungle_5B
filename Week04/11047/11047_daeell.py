import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input())for _ in range(n)]
coins.sort(reverse=True)

ans = 0
while k > 0:
    for coin in coins:
        ans += k // coin
        k = k % coin
        if k == 0:
            break
print(ans)
