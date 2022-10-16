import sys
sys.stdin = open('Week04/9251/9251_lwh.txt', 'r')
input = sys.stdin.readline

arr1 = input().rstrip()
arr2 = input().rstrip()

n = len(arr1)
m = len(arr2)

dp = [[0]*(m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
