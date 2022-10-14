# 동전

# 금액의 오름차순으로 정렬된 동전들을 차례대로 사용할 때
# 이전에 계산된 각 금액에 대한 경우의 수는 누적해서 갱신되므로
# dp를 1차원 리스트로 선언해서 
# 현재 순회중인 동전을 이용한 경우의 수를 매 순회마다 누적한다면
# 결국 주어진 금액을 만들기 위한 경우의 수를 구할 수 있음

import sys

input = sys.stdin.readline
print = sys.stdout.write

tc = int(input().rstrip())

while tc > 0:
    n = int(input().rstrip())
    tmp = list(map(int, input().split()))
    m = int(input().rstrip())

    dp = [0] * (m+1)
    dp[0] = 1

    for t in tmp:
        for j in range(t, m+1):
            dp[j] += dp[j-t]

    print(f"{dp[m]}\n")
    tc -= 1
