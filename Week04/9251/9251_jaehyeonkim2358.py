import sys

sequence1 = sys.stdin.readline().rstrip()
sequence2 = sys.stdin.readline().rstrip()

n = len(sequence1)
m = len(sequence2)

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    s1 = sequence1[i-1]
    for j in range(1, m+1):
        s2 = sequence2[j-1]
        if s1 == s2:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

sys.stdout.write(f'{dp[n][m]}')