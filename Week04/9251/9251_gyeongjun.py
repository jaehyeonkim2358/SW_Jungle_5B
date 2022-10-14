from collections import deque
import sys
input = sys.stdin.readline

strr = list(input().rstrip())
strr2 = list(input().rstrip())

dp = [[0] * (len(strr2)+1) for _ in range(len(strr)+1)]

flag = False

for i in range(1, len(strr)+1):
    for j in range(1, len(strr2)+1):
        if(strr[i-1] == strr2[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
print(dp[-1][-1])

