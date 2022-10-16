import sys
input = sys.stdin.readline
def greedy(k, coin):
    cnt = 0
    for _ in range(n):
        now = coin.pop()
        cnt += k // now
        k = k % now
    return cnt

if __name__ == '__main__':
    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]

    print(greedy(k, coin))