import sys

input = sys.stdin.readline
print = sys.stdout.write

tc = int(input().rstrip())

while tc > 0:
    n = int(input().rstrip())
    tmp = list(map(int, input().split()))
    m = int(input().rstrip())
    coin = []
    for t in tmp:
        if t > m:
            break
        coin.append(t)

    n = len(coin)

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1                    # 현재 동전을 사용하지 않는 경우의 수
        cur_cost = coin[i-1]
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]               # 이전 동전으로 계산된 경우의 수를 그대로 내려줌
            if j >= cur_cost:                   # 현재 동전값 이상인 금액에 대해서
                dp[i][j] += dp[i][j-cur_cost]   # 현재 동전을 사용해서 해당 금액을 만드는 경우의 수를 더해줌

    print(f"{dp[n][m]}\n")
    tc -= 1
