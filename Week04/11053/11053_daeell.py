import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
dp = [1] * (n)

for i in range(1, n):
    for j in range(i):
        # 자기 앞에 있는 요소들을 비교한다.
        if a_list[j] < a_list[i]:
            # 현재 숫자가 앞에 있는 숫자보다 크다면
            dp[i] = max(dp[i], dp[j]+1)
            # 현재 가장 긴 배열에 붙는 것을 선택한다.

print(max(dp))
