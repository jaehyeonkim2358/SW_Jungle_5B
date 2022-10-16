import sys
sys.stdin = open('Week04/11053/11053_lwh.txt', 'r')
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp))