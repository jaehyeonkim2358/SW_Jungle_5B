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

    # 금액의 오름차순으로 정렬된 동전들을 차례대로 사용할 때
    # 이전에 계산된 각 금액에 대한 경우의 수는 누적해서 갱신되므로
    # dp를 1차원 리스트로 선언해서 
    # 현재 순회중인 동전을 이용한 경우의 수를 매 순회마다 누적한다면
    # 결국 주어진 금액을 만들기 위한 경우의 수를 구할 수 있음
    dp = [0] * (m+1)
    dp[0] = 1

    for i in range(1, n+1):
        cur_cost = coin[i-1]
        for j in range(1, m+1):
            if j >= cur_cost:
                dp[j] += dp[j-cur_cost]

    print(f"{dp[m]}\n")
    tc -= 1
