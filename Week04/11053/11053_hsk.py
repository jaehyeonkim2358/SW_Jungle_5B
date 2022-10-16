import sys
sys.stdin = open("input.txt","r")
# 07. https://www.acmicpc.net/problem/11053: 가장 긴 증가하는 부분 수열
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split())) 

dp = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
print(dp)