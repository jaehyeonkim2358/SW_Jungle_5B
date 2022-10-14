import sys
input = sys.stdin.readline
k = int(input())
for i in range(k):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(arr[i], m+1):
            now = dp[j - arr[i]]
            dp[j] += now
    print(dp[m])

