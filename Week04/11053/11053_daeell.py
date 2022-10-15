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
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
