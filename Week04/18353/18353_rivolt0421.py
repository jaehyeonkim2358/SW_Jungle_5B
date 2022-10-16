import sys
sys.stdin = open("W03-W04/Week04/18353/input.txt","r")

dp = [1] * (n := int(input()))
l = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if l[j] > l[i]: # 감소하는 부분수열 이므로.
            dp[i] = max(dp[j] + 1 , dp[i])

print(n-max(dp))